import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
title=driver.title
print(title)
url=driver.current_url
print(url)
#---------------USING CLASS-----------------------------
# it gives error because space is there so you dont go this method if space is not there in class you can use that
#otherwise it is best to go with xPATH Locator

#---------------USING XPATH--------------------
#1.ABSOLUTE XPATH (It is not feasible because syntax is very high)
#2.RELATIVE XPATH (it is feasible method compared to absolute xpath)

#---------------USING RELATIVE XPATH-----------------
txtuser = driver.find_element(By.CLASS_NAME, "inputtext _55r1 _6luy")
txtuser.send_keys("anithavinoth")

#TO ENTER EMAIL OR USERNAME
txtuser = driver.find_element(By.XPATH, "//input[@id='email']")
txtuser.send_keys("anithavinoth")

#TO ENTER PASSWORD
txtpass = driver.find_element(By.XPATH, "//input[@type='password']")
txtpass.send_keys("123456789")

#TO CLICK LOGIN BUTTON
btnlogin = driver.find_element(By.XPATH, "//button[@type='submit']")
btnlogin.click()

#TO CLICK CREATE BUTTON There are 2 ways to write a code
# way 1 web element (using slice operator to find the exact element)
creatbtn = driver.find_element(By.XPATH,"(//a[@role='button'])[2]")
creatbtn.click()
#way 2 list of web element (using index method to find the exact element)
createbtn = driver.find_elements(By.XPATH, "//a[@role='button']")
listofwebelement = createbtn[1]
listofwebelement.click()

time.sleep(6)