import time

from selenium import webdriver

driver = webdriver.Chrome()


driver.get("https://www.facebook.com")
title = driver.title
print(title)
url = driver.current_url
print(url)
time.sleep(6)