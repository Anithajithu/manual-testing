from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
#by using XPATH text
crtpge = driver.find_element(By.XPATH, "//a[text()='Create a Page']")
t = crtpge.text
print(t)

#By using XPATH Contains for text

