from db import Db
import itemsql


class ItemDb(Db):
    def __init__(self, dbname):
        super().__init__(dbname)
        super().makeTable()

    def insert(self, item):
        cs = None
        con = None
        try:
            con = self.connect()
            cs = con.cursor()
            cs.execute(item.getInsert().strip())
            con.commit()
        except:
            raise Exception
        finally:
            super().close(cs, con)

    def update(self, item):
        cs = None
        con = None
        try:
            con = self.connect()
            cs = con.cursor()
            cs.execute(item.getUpdate().strip())
            con.commit()
        except:
            raise Exception
        finally:
            super().close(cs, con)

    def delete(self, ids):
        cs = None
        con = None
        try:
            con = self.connect()
            cs = con.cursor()
            cs.execute(itemsql.ITEM_DELETE % ids)
            con.commit()
        except:
            raise Exception
        finally:
            super().close(cs, con)

    def select(self):
        cs = None
        con = None
        try:
            con = self.connect()
            cs = con.cursor()
            cs.execute(itemsql.ITEM_SELETE)
            results = cs.fetchall()
        except:
            raise Exception
        finally:
            super().close(cs, con)
        return results

    def selectOne(self, ids):
        cs = None
        con = None
        try:
            con = self.connect()
            cs = con.cursor()
            cs.execute(itemsql.ITEM_SLETE_ONE % ids)
            datas = cs.fetchall()
            for i in datas:
                print(i)
        except:
            raise Exception
        finally:
            super().close(cs, con)
        return datas

