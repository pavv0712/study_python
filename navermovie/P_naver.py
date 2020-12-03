import time
from adp_movie import Insertmovie, Existmovie
from adp_staff import Insertstaff, Existstaff

def Selemoviedetail(code, driver):
    
    Isexistmovie = Existmovie(code)

    if Isexistmovie == True:
        return

    d_url = 'https://movie.naver.com/movie/bi/mi/basic.nhn?code={0}'
    driver.get(d_url.format(code))
    
    dds = driver.find_elements_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd')
    
    _rating = ''
    if len(dds) == 3:
        _rating = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[3]/p').text
    else : 
        _rating = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[4]/p').text

    
    _code = code
    
    _title = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/h3/a').text
    
    _story = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[4]/div[1]/div/div[1]').text
	
    spans = driver.find_elements_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span')
    
    _op_dt = ''

    if len(spans) == 4:
        _op_dt =driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[4]').text
        _genre = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[1]').text
        _rn_tm = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[3]').text

    elif len(spans) == 3:
        _op_dt = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[3]').text
        _genre = ''
        _rn_tm = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[2]').text


    # print(_code, _title, _story, _genre, _rating, _rn_tm, _op_dt)

    time.sleep(5)


    Insertmovie(_code, _title, _story, _genre, _rating, _rn_tm, _op_dt)




def Selemovie(driver):

        url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200803&page={0}'
        
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
                Selemoviedetail(code, driver)
                
            
            ispage = False
            page = page + 1

def Selestaff(movie, driver):
     d_url = 'https://movie.naver.com/movie/bi/mi/detail.nhn?code={0}'
     driver.get(d_url.format(movie.code))
     time.sleep(3)
     act_more = driver.find_element_by_xpath('//*[@id="actorMore"]').click()
     
     time.sleep(3)
     
     act_list = driver.find_elements_by_xpath('//*[@id="content"]/div[1]/div[4]')
     for act in act_list:
         href = act.find_element_by_xpath('//*[@id="content"]/div/ul/li/a').get_attribute('href')
         _s_code = href.split('=')[1]
         _k_name = act.find_element_by_xpath('.//*[@class = "k_name"]').text
         _e_name = act.find_element_by_xpath('.//*[@class = "e_name"]').text
        
         try:
            _cast_name = act.find_element_by_xpath('.//*[@class = "pe_cmt"]')

         except:
            _cast_name = '없음'
         _birth = ''
         _nation = ''
         _role_info = act.find_element_by_xpath('.//*[@class = "pe_cmt"]')
         _is_director = False
         _is_actor = True
        
         Isexist = Existstaff(_s_code)
        
         if Isexist == False:

            Insertstaff(_s_code, _k_name, _e_name, _birth, _nation, _is_director, _is_actor)

                
     time.sleep(10)