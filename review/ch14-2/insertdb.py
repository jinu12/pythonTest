import sqlite3
con = None
cs = None
try:
    con = sqlite3.connect('addr.db')
    cs = con.cursor()
    insertsql = 'INSERT INTO tb_addr VALUES("%s", "%s", "%s")'
    name = input('Inpput Name....')
    phone = input('Inpput Name....')
    addr = input('Inpput Name....')
    cs.execute(insertsql % (name, phone, addr))
    con.commit()
except:
    print('Error')
    raise
finally:
    if cs is not None:
        cs.close()
    if con is not None:
        con.close()
