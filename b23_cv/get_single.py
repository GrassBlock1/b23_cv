import os

import markdownify
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from b23_cv import cleanup_filename
from b23_cv.download_image import download_image
from b23_cv.init_driver import init_driver


def __main__(stdin_url, stdin_folder):
    passage_url = stdin_url  # 目标网页
    output_folder = stdin_folder  # 存放Markdown文件的文件夹

    # 初始化Selenium WebDriver
    driver = init_driver()

    driver.get(passage_url)  # 访问目标网页

    # 等待 'article-item' 元素加载
    wait = WebDriverWait(driver, 10)
    wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'article-content')))

    content_element = driver.find_element(By.ID, 'article-content')
    html_content = content_element.get_attribute('outerHTML')
    title = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/div[1]/h1').get_attribute('innerText')

    print(f'[debug] Get {title}')

    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    print("[debug] Processing images for", title)
    # 创建存放图片的文件夹
    img_folder = os.path.join(output_folder, 'img')
    os.makedirs(img_folder, exist_ok=True)

    # 替换HTML中的图片链接并下载图片
    for img in soup.find_all('img'):
        img_url = 'https:' + img['data-src']
        local_img_path = download_image(img_url, img_folder)
        if local_img_path:
            img['src'] = os.path.relpath(local_img_path, start=output_folder)

    # 将HTML内容转换为Markdown
    markdown_content = markdownify.markdownify(str(soup), heading_style="ATX")

    # 尝试解决标题中包含 / 等特殊字符时无法保存的问题
    file_name = cleanup_filename.sanitize_filename(title)

    # 保存Markdown内容到文件
    markdown_file_path = os.path.join(output_folder, f'{file_name}.md')
    with open(markdown_file_path, 'w+', encoding='utf-8') as f:
        f.write(markdown_content)
    print(f'Saved {markdown_file_path}')

    driver.back()  # 返回上一页

    print('Done!')
    # 关闭Selenium WebDriver
    driver.quit()
