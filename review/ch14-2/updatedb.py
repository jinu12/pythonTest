import sqlite3
con = None
cs = None
try:
    con = sqlite3.connect('addr.db')
    cs = con.cursor()
    updatesql = 'UPDATE tb_addr SET phone="%s", addr= "%s" WHERE name= "%s"'
    name = input('Inpput Phone....')
    phone = input('Inpput addr....')
    addr = input('Inpput name....')
    cs.execute(updatesql % (phone, addr, name))
    con.commit()
except:
    print('Error')
finally:
    if cs is not None:
        cs.close()
    if con is not None:
        con.close()
