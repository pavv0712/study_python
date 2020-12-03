from selenium import webdriver
from adp_movie2 import Searchmovie, Insertmovie, Existmovie
from adp_staff import Searchstaff
from crawling_movie import Movie
from crawling_staff import Stafflist
from movie_html import CreatemovieHtml, MovieHtmlDetail
import pymssql


command = ''

driver = webdriver.Chrome()
while command != 'EXIT':
    command = input('명령입력요망')

    if command == '1':
        Movie(driver)
        
            # count = 1
        # ms = Searchmovie()
        # for m in ms:
        #     m.show(count)
        #     count += 1

    elif command == '2':
        sm = Searchstaff()
        for s in sm:
            s.show()

    elif command == '4':
        mov = Searchmovie()       

        count = 1
        for m in mov:
            m.show(count)
            count = count + 1
            
            Stafflist(m, driver)

    elif command == '5':
        
        CreatemovieHtml(Searchmovie())
        print('저장완료')


    elif command == '6':
        MovieHtmlDetail(Searchstaff())



   
   

    
        


