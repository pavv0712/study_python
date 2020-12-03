import pymssql
from model_movie import Movie

ip = 'localhost'
id = 'sa'
pw = '!mssql1234'
db = 'NAVER'

def Existmovie(code):

    conn = pymssql.connect(server=ip, user=id, password=pw, database=db)
    cursor = conn.cursor()
    query = 'SELECT CODE FROM MOVIE WHERE CODE = %s'
    cursor.execute(query, code)

    Isexist = False

    row = cursor.fetchone()
    while row:
        Isexist = True
        break
    return Isexist

def Insertmovie(_code, _title, _story, _genre, _rating, _rn_tm, _op_dt):

    opdt = _op_dt.split(',')

    if len(opdt) > 1:
        _op_dt = opdt[-1]

    _rn_tm = _rn_tm.replace('분','')
    _op_dt = _op_dt.replace(' ','').replace('개봉','').replace('.','-')
    
    if len(_op_dt) == 7:
        _op_dt += '-01'

    conn = pymssql.connect(server=ip, user=id, password=pw, database=db)
    cursor = conn.cursor()
    query = '''
        INSERT MOVIE(CODE, TITLE, STORY, GENRE, RATING, RN_TM, OP_DT)
	    VALUES(%s, %s, %s, %s, %s, %s, %s)
        '''
    cursor.execute(query, (_code, _title, _story, _genre, _rating, _rn_tm, _op_dt))
    conn.commit()


def Searchmovie():
    
    conn = pymssql.connect(server=ip, user=id, password=pw, database=db)
    cursor = conn.cursor()
    query = 'SELECT * FROM MOVIE'
    cursor.execute(query)

    movie_list =  list()
    row = cursor.fetchone()

    while row:
        _code = row[0]
        _title = row[1]
        _story = row[2]
        _genre = row[3]
        _rating = row[4]
        _rn_tm = row[5]
        _op_dt = row[6]

        mov = Movie(_code, _title, _story, _genre, _rating, _rn_tm, _op_dt)
        movie_list.append(mov)
        row = cursor.fetchone()
    return movie_list


