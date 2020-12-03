import pymssql
from model_staff import Staff



ip = 'localhost'
id = 'sa'
pw = '!mssql1234'
db = 'NAVER_2'

def Existstaff(code):
    
    
    conn = pymssql.connect(server=ip, user=id, password=pw, database=db)
    cursor = conn.cursor()
    query = 'SELECT CODE FROM STAFF WHERE CODE = %s'
    cursor.execute(query, code)
    
    Isexiststaff = False

    row = cursor.fetchone()
    
    while row:
        Isexiststaff = True
        break
    return Isexiststaff



def Searchstaff():
    
    conn = pymssql.connect(server=ip, user=id, password=pw, database=db)
    cursor = conn.cursor()
    query = 'SELECT * FROM STAFF'
    cursor.execute(query)

    staff_list = list()

    row = cursor.fetchone()

    while row:
        _s_code = row[0]
        _k_name = row[1] 
        _e_name = row[2]

        sta = Staff(_s_code, _k_name, _e_name)
        staff_list.append(sta)
        row = cursor.fetchone()

    return staff_list



def Insertstaff(_s_code, _k_name, _e_name):
    
    conn = pymssql.connect(server=ip, user=id, password=pw, database=db)
    cursor = conn.cursor()
    query = '''
        INSERT STAFF(CODE, K_NAME, E_NAME)
        VALUES(%s, %s, %s) 
        '''
    cursor.execute(query, (_s_code, _k_name, _e_name))
    conn.commit()
