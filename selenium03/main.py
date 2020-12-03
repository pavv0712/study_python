import time
from selenium import webdriver
from model_actor import Actor
from model_movie import Movie



driver = webdriver.Chrome()

list_url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200729&page={0}'
ispage = True
count = 0

while ispage == True:
    
    count = count + 1

    driver.get(list_url.format(count))

    table = driver.find_element_by_xpath('//*[@id="old_content"]/table')
    tbody = table.find_element_by_xpath('.//tbody')
    trs = tbody.find_elements_by_xpath('.//tr')
    urls = list()

    for tr in trs:
        tds = tr.find_elements_by_xpath('.//td')
        
        if len(tds) == 1:
            continue

        div = tds[1].find_element_by_xpath('.//div')
        a = div.find_element_by_xpath('.//a')
        href = a.get_attribute('href')

        urls.append(href)




    movies = list()

    for url in urls:
        driver.get(url)

        actor = driver.find_element_by_xpath('//*[@id="movieEndTabMenu"]/li[2]/a').click()

        title = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/h3/a')

        
        try:
            more_actor = driver.find_element_by_xpath('//*[@id="actorMore"]').click()
        except:
            pass


        lis = driver.find_elements_by_xpath('//*[@id="content"]/div[1]/div[4]/div[1]/div/div[2]/ul/li')

        act_list = list()


        for li in lis:
            
        
            actname = li.find_element_by_xpath('.//*[@class="k_name"]')
            ename = li.find_element_by_xpath('.//*[@class="e_name"]')
            p_part = li.find_element_by_xpath('.//*[@class="p_part"]')
            p_cmt = ''

            try:
                p_cmt = li.find_element_by_xpath('.//*[@class="pe_cmt"]').text
            except:
                p_cmt = None
            
            
            

            act = Actor(actname, ename.text, p_part.text, p_cmt)
        
            act_list.append(act)


        mov = Movie(title.text, act_list)
        
        movies.append(mov)


        print('완료: {0}, 배우: {1}명'.format(mov.title, len(mov.acts)))
        
        
print('{0} 완료'.format(count))
        