import pymssql
from model_k_table import Table

ip = 'localhost'
id = 'sa'
pw = '!mssql1234'
db = 'kle'




def Searchtable():
    
    tables = list()

    conn = pymssql.connect(server=ip, user=id, password=pw, database=db)

    cursor = conn.cursor()
    
    cursor.execute('SELECT *FROM KLEAGUE_DAY')

    row = cursor.fetchone()

    while row:
           _rank = row[0] 
           _name = row[1]
           _round =row[2]
           _point = row[3]
           _win = row[4]
           _draw = row[5]
           _lose = row[6]
           _gf = row[7]
           _gc = row[8]
           _gd = row[9]
           _help = row[10]
           _foul = row[11]

           
           ta = Table(_rank, _name, _round, _point, _win, _draw, _lose, _gf, _gc, _gd, _help, _foul)
           tables.append(ta)
           row = cursor.fetchone()
    
    return tables
