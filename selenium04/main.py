import time 
from company import loadcompany
from down import download
from selenium import webdriver
from stock import createstockhtml

driver = webdriver.Chrome()

coms = loadcompany()


for com in coms:

    print('{0}({1}) 시작'.format(com.symbol, com.name))
    
    download(driver, com.symbol)
    time.sleep(10)
    createhtml(com.symbol)

