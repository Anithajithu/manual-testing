import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
print("DayTwoCompleted")
driver.get("https://www.facebook.com")
title = driver.title
print(title)
url = driver.current_url
print(url)

# -------------ID--------------

# txtuser = driver.find_element(By.ID, "email")
# txtuser.send_keys("anithabeec@gmail.com")

# txtpassword = driver.find_element(By.ID, "pass")
# txtpassword.send_keys("anitha6")

# btnlogin = driver.find_element(By.ID, "u_0_5_/F")
# btnlogin.click()
#CLICK login button give error in ID locator because the value(u_0_5_/F)in ID is changing everytime
#while clicking the refresh button in homepage web browser.


#------------------NAME------------
txtuser = driver.find_element(By.NAME, "email")
txtuser.send_keys("vinothkumarbaskar6@gmail.com")

txtpass = driver.find_element(By.NAME, "pass")
txtpass.send_keys("123456")

btnlogin = driver.find_element(By.NAME, "login")
btnlogin.click()

time.sleep(10)
driver.quit()
