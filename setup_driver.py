#from selenium.webdriver.firefox.options import Options
#from selenium.webdriver.firefox.service import Service

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


def chrome_driver():
    s = Service('/Users/cindyhuang/Downloads/chromedriver')
    driver = webdriver.Chrome(service=s)
    return driver

def firefox_driver():
    driver_path = "./drivers/geckodriver.exe"
    firefox_service = Service(driver_path)
    firefox_options = Options()
    firefox_options.headless = True
    driver = webdriver.Firefox(service=firefox_service, options=firefox_options)
    return driver
