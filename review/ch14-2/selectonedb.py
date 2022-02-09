import sqlite3
con = None
cs = None
try:
    con = sqlite3.connect('addr.db')
    cs = con.cursor()
    selectsql = 'SELECT * FROM tb_addr WHERE name = "%s"'
    name = input('Inpput Name....')
    cs.execute(selectsql % name)
    datas = cs.fetchall()
    for data in datas:
        print(data)
except:
    print('Error')
finally:
    if cs is not None:
        cs.close()
    if con is not None:
        con.close()
