from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()

name = driver.find_element(By.NAME, "fName")
name.send_keys("asd")

surname = driver.find_element(By.NAME, "lName")
surname.send_keys("jkl")

email = driver.find_element(By.NAME, "email")
email.send_keys("1@2.com")

sign_up = driver.find_element(By.CSS_SELECTOR, ".form-signin button")
sign_up.send_keys(Keys.ENTER)
