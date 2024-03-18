from selenium import webdriver
from selenium.webdriver.common.by import By

edge = webdriver.Edge()
edge.get("https://www.instagram.com")
edge_title = edge.title
print(edge_title)
url = edge.current_url
print(url)

txtuser = edge.find_element(By.XPATH, "(//input[@aria-required='true'])[1]")
txtuser.send_keys("anitha")

txtpass = edge.find_elements(By.XPATH, "//input[@aria-required='true']")
wb=txtpass[1]
# wb.send_keys("12345")

l = edge.find_element(By.XPATH, "//div[text()='Log in']")
l.click()




