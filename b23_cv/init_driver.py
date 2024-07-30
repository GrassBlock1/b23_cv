# 初始化Selenium WebDriver
from selenium.webdriver import FirefoxProfile
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def init_driver():
    options = Options()
    options.add_argument('-headless')
    firefox_profile = FirefoxProfile()
    firefox_profile.set_preference("network.proxy.type", '0')
    options.profile = firefox_profile

    service = webdriver.FirefoxService(
        service_args=['--log', 'debug'])  # 替换为实际的firefox路径
    driver = webdriver.Firefox(service=service, options=options)
    return driver
