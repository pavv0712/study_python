from selenium import webdriver
from model_movie import Movie

movies = list()


driver = webdriver.Chrome()

driver.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')

table = driver.find_element_by_xpath('//*[@id="old_content"]/table')

trs = table.find_elements_by_xpath('.//tr')



for tr in trs:
    
    tds = tr.find_elements_by_xpath('.//td')
    

    if len(tds) == 0:
        continue
    if len(tds) == 1:
        continue
    
    img = tds[0].find_element_by_xpath('.//img')
    alt = img.get_attribute('alt')
    rank = int(alt)
    
    
    title = tds[1].text
    movie = Movie(title, rank)
    movies.append(movie)
    
driver.quit()
  

for m in movies:
    print('{0}:{1}'.format(m.rank, m.title))