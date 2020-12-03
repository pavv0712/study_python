from selenium import webdriver
from adp_movie2 import Insertmovie,Existmovie
import time


def Moviedetail(code, driver):

    Isexist = Existmovie(code)
    
    if Isexist == True:
        return


    d_url = 'https://movie.naver.com/movie/bi/mi/basic.nhn?code={0}'
    driver.get(d_url.format(code))
    _code = code
    _title = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/h3/a').text
    _genre = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[1]').text
    _story = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[4]/div[1]/div/div/p').text
    _img_src = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[2]/a/img').get_attribute('src')
    
    time.sleep(5)

    Insertmovie(_code, _title, _genre, _story, _img_src)


def Movie(driver):
    
    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200804&page={0}'

    page = 1
    ispage = True
    m_code_list = list()

    while ispage == True:
        driver.get(url.format(page))


        table = driver.find_element_by_xpath('//*[@id="old_content"]/table')
        trs = table.find_elements_by_xpath('.//tr')
    
        for tr in trs:
            tds = tr.find_elements_by_xpath('.//td')
            if len(tds) == 0:
                continue
            elif len(tds) == 1:
                continue

            href = tds[1].find_element_by_xpath('.//div/a').get_attribute('href')
        
            m_code = href.split('=')[1]

            m_code_list.append(m_code)

        for code in m_code_list:
            Moviedetail(code, driver)

        page = page + 1


