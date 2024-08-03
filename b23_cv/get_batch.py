import os
from urllib.parse import urljoin, urlparse

import markdownify
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from b23_cv import cleanup_filename, convert_article
from b23_cv.download_image import download_image
from b23_cv.init_driver import init_driver


def __main__(stdin_url, stdin_folder, stdin_format):
    list_url = stdin_url
    output_folder = stdin_folder
    output_format = stdin_format

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

        convert_article.__main__(html_content, title, output_format, output_folder)

        driver.back()  # 返回上一页

    print('All done!')
    # 关闭Selenium WebDriver
    driver.quit()
