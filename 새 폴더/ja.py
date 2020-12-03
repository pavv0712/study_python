from selenium import webdriver

driver = webdriver.Chrome()

james = driver.find_elements_by_xpath('//*[@id="americaIndex"]’')

print(type(james))