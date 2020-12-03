import pymssql
from model_k_league import League

ip = 'localhost'
id = 'sa'
pw = '!mssql1234'
db = 'kle'

def Searchteam():

    conn = pymssql.connect(server=ip, user=id, password=pw, database=db)

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM TEAM')

    leagues = list()

    row = cursor.fetchone()

    while row:

        _name = row[0]
        _year = row[1]
        _coach =  row[2]
        _captain = row[3]
        _top_socorer = row[4]
        _top_helper = row[5]
        
        lea = League(_name, _year, _coach, _captain, _top_socorer, _top_helper)
        leagues.append(lea)
        row = cursor.fetchone()

    return leagues