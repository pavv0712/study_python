import time
import shutil
from os import path



def download(driver, code):

    url = 'https://finance.yahoo.com/quote/{0}/history?p={0}'

    

    driver.get(url.format(code))

    time.sleep(3)

    isselect = False
    while isselect == False:
        try:
            select = driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[1]/div[1]/div/div')
            select.click()
            isselect = True
        except:
            time.sleep(3)

    btn_max = driver.find_element_by_xpath('//*[@id="dropdown-menu"]/div/ul[2]/li[4]/button')
    btn_max.click()

    time.sleep(3)

    btn_apl = driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[1]/button')
    btn_apl.click()

    time.sleep(3)

    btn_dwn = driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[2]/span[2]/a')
    btn_dwn.click()

    time.sleep(3)


    filename = '{0}.csv'.format(code)
    src = 'C:/Users/ASIA_01/Downloads/{0}'.format(filename)
    dir = 'C:/python/finance/{0}'.format(filename)

    isexists = False
    while isexists == False:
        isexists = path.exists(src)
        time.sleep(1)

    
    
    
    shutil.move(src, dir)

