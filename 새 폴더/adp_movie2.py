import pymssql
from model_movie2 import Movie2

ip = 'localhost'
id = 'sa'
pw = '!mssql1234'
db = 'NAVER_2'

def Searchmovie():

    conn = pymssql.connect(server=ip, user=id, password=pw, database=db)
    cursor = conn.cursor()
    query = 'SELECT * FROM MOVIE_2'
    cursor.execute(query)

    movie_list = list()

    row = cursor.fetchone()

    while row:

        _code = row[0]
        _title = row[1]
        _genre = row[2]
        _story = row[3]
        _img_src = row[4]
        mov = Movie2(_code, _title, _genre, _story, _img_src)
        movie_list.append(mov)
        row = cursor.fetchone()

    return movie_list
        
def Insertmovie(_code, _title, _genre, _story, _img_src):

    conn = pymssql.connect(server=ip, user=id, password=pw, database=db)
    cursor = conn.cursor()
    query = '''
    INSERT MOVIE_2(CODE, TITLE, GENRE, STORY, IMG)
    VALUES(%s, %s, %s, %s, %s)
    '''
    cursor.execute(query, (_code, _title, _genre, _story, _img_src))
    conn.commit()

def Existmovie(code):
    conn = pymssql.connect(server=ip, user=id, password=pw, database=db)
    cursor = conn.cursor()
    query = 'SELECT CODE FROM MOVIE_2 WHERE CODE = %s'
    cursor.execute(query, code)

    row = cursor.fetchone()
    Isexist = False
   
    while row: #!= None 
        Isexist = True
        break
        
    return Isexist 




