from selenium import webdriver

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

dates = driver.find_elements_by_css_selector("div .shrubbery ul time")
titles = driver.find_elements_by_css_selector("div .shrubbery ul a")

# for (date, title) in zip(dates, titles):
#     print(date.text, title.text)

events = {}
index = 0
for date, title in zip(dates, titles):
    events[index] = {"time": date.text, "name": title.text}
    index += 1

print(events)

# driver.close()
driver.quit()
