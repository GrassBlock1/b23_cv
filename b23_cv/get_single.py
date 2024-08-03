import os

import markdownify
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from b23_cv import convert_article
from b23_cv.init_driver import init_driver


def __main__(stdin_url, stdin_folder, stdin_format):
    passage_url = stdin_url  # 目标网页
    output_folder = stdin_folder  # 存放Markdown文件的文件夹
    output_format = stdin_format  # 输出格式

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

    convert_article.__main__(html_content, title, output_format, output_folder)

    driver.back()  # 返回上一页

    print('Done!')
    # 关闭Selenium WebDriver
    driver.quit()
