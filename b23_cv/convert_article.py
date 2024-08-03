import os
import shutil

import markdownify
from bs4 import BeautifulSoup

from b23_cv import cleanup_filename
from b23_cv.download_image import download_image


def __main__(html_content, title, export_format, output_folder):
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    print("[debug] Processing images for", title)
    # 创建存放图片的文件夹
    img_folder = os.path.join(output_folder, 'img')
    os.makedirs(img_folder, exist_ok=True)

    # 替换HTML中的图片链接并下载图片
    for img in soup.find_all('img'):
        if not img.has_attr('data-src'):
            img_url = img['src']
        else:
            img_url = 'https:' + img['data-src']
        local_img_path = download_image(img_url, img_folder)
        if local_img_path:
            img['src'] = os.path.relpath(local_img_path, start=output_folder)

    if export_format == "markdown":
        # 将HTML内容转换为Markdown
        markdown_content = markdownify.markdownify(str(soup), heading_style="ATX")

        # 尝试解决标题中包含 / 等特殊字符时无法保存的问题
        file_name = cleanup_filename.sanitize_filename(title)

        # 保存Markdown内容到文件
        markdown_file_path = os.path.join(output_folder, f'{file_name}.md')
        with open(markdown_file_path, 'w+', encoding='utf-8') as f:
            f.write(markdown_content)
        print(f'Saved {markdown_file_path}')
    else:
        # 尝试解决标题中包含 / 等特殊字符时无法保存的问题
        file_name = cleanup_filename.sanitize_filename(title)
        # 保存HTML内容到文件
        html_file_path = os.path.join(output_folder, f'{file_name}.html')
        html_body = f"""<h1 id="title">{title}</h1><br>{str(soup)}"""
        html = f"""<!DOCTYPE html>
        <html lang="zh-CN">
        <head>
            <meta charset="UTF-8">
            <title>{title}</title>
            <link rel="stylesheet" href="css/article.css">
            </head>
            <body>
            {html_body}
            </body>
            </html>
        """
        os.makedirs(os.path.join(output_folder, 'css'), exist_ok=True)
        shutil.copy('html/css/article.css', os.path.join(output_folder, 'css/article.css'))
        with open(html_file_path, 'w+', encoding='utf-8') as f:
            f.write(html)
        print(f'Saved {html_file_path}')
