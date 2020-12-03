import time
from adp_staff import Insertstaff,Existstaff


def Stafflist(movie, driver):

    s_url = 'https://movie.naver.com/movie/bi/mi/detail.nhn?code={0}'

    driver.get(s_url.format(movie.code))
    
    time.sleep(5)

    act_more = ''
   
    try:
         driver.find_element_by_xpath('//*[@id="actorMore"]').click()
    except:
        pass
    time.sleep(5)

    lis = driver.find_elements_by_xpath('//*[@id="content"]/div[1]/div[4]/div[1]/div/div[2]/ul/li')
    
    for act in lis:

        a = act.find_element_by_xpath('.//div/a')
        href = a.get_attribute('href')
        _s_code = href.split('=')[1]     
        _k_name = act.find_element_by_xpath('.//*[@class="k_name"]').text 
        
        try:
            _e_name = act.find_element_by_xpath('.//*[@class="e_name"]').text
        except:
            pass

        Isexiststaff = Existstaff(_s_code) 

        if Isexiststaff == False:
            Insertstaff(_s_code, _k_name, _e_name)

    time.sleep(3)

       








