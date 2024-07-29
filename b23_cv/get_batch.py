import os
from urllib.parse import urljoin, urlparse

import markdownify
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from b23_cv.download_image import download_image
from b23_cv.init_driver import init_driver


def __main__(stdin_url, stdin_folder):
    list_url = stdin_url
    output_folder = stdin_folder

    # 初始化Selenium WebDriver
    driver = init_driver()

    driver.get(list_url)  # 访问目标网页

    # 等待 'article-item' 元素加载
    wait = WebDriverWait(driver, 10)
    wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'article-item')))

    # 抓取所有包含 'read/cv' 的链接
    links_element = driver.find_elements(By.XPATH, "//a[contains(@href, 'read/cv')]")
    links = []
    for i in links_element:
        link = i.get_attribute('href')
        url = urljoin(link, urlparse(link).path)
        full_url = urljoin('https:', url)  # 确保链接是完整的URL
        filtered_url = full_url.rstrip('/')
        if filtered_url not in links:
            links.append(filtered_url)

    print(f'[debug] Found {len(links)} passages.')
    # 使用集合来存储已处理过的URL

    for i in range(len(links)):
        if i >= len(links):
            print("Oh no...Seems to be the last link...maybe the length of the list is wrong...")
            break
        full_url = links[i]
        driver.get(full_url)

        # 抓取id为 'article-content' 的HTML元素
        content_element = driver.find_element(By.ID, 'article-content')
        html_content = content_element.get_attribute('outerHTML')
        title = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/div[1]/h1').get_attribute(
            'innerText')
        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        print("[debug] Processing images for", title)
        # 创建存放图片的文件夹
        parsed_url = urlparse(full_url)
        cv_id = full_url.split('/')[-1]
        img_folder = os.path.join(output_folder, 'img', cv_id)
        os.makedirs(img_folder, exist_ok=True)

        # 替换HTML中的图片链接并下载图片
        for img in soup.find_all('img'):
            img_url = urljoin(full_url, img['data-src'])
            local_img_path = download_image(img_url, img_folder)
            if local_img_path:
                img['src'] = os.path.relpath(local_img_path, start=output_folder)

        # 将HTML内容转换为Markdown
        markdown_content = markdownify.markdownify(str(soup), heading_style="ATX")

        # 保存Markdown内容到文件
        markdown_file_path = os.path.join(output_folder, f'{title}.md')
        with open(markdown_file_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        print(f'Saved {markdown_file_path}')

        driver.back()  # 返回上一页

    print('All done!')
    # 关闭Selenium WebDriver
    driver.quit()
