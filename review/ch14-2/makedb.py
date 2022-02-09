import sqlite3

con = sqlite3.connect('addr.db')
cs = con.cursor()
dropsql = 'DROP TABLE IF EXISTS tb_addr'
createesql = """
    CREATE TABLE tb_addr (
        name CHAR(16) PRIMARY KEY,
        phone CHAR(16),
        addr TEXT
)"""

cs.execute(dropsql)
cs.execute(createesql)
con.commit()

cs.close()
con.close()
