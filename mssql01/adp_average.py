import pymssql
from model_average import Average

ip = 'localhost'
id = 'sa'
pw = '!mssql1234'
db = 'kle'

def Searchaverage():

    conn = pymssql.connect(server=ip, user=id, password=pw, database=db)

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM AVERAGE')

    averages = list()

    row = cursor.fetchone()

    while row:

        _win = row[0]
        _draw = row[1]
        _lose =  row[2]
     
        ave = Average(_win, _draw, _lose)
        averages.append(ave)
        row = cursor.fetchone()

    return averages