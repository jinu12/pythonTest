import sqlite3
import itemsql


def connect(dbname):
    con = sqlite3.connect(dbname)
    return con


def close(*cs):
    for c in cs:
        if c is not None:
            c.close()


def makeTable(name):
    cs = None
    con = None
    try:
        con = connect(name)
        cs = con.cursor()
        cs.execute(itemsql.MAKE_TABLE)
        con.commit()
    except:
        raise Exception
    finally:
        close(cs, con)
    return None


def insert(*datas):
    cs = None
    con = None
    try:
        con = connect('item.db')
        cs = con.cursor()
        cs.execute(itemsql.ITEM_INSERT % datas)
        con.commit()
    except:
        raise Exception
    finally:
        close(cs, con)


def delete(*datas):
    cs = None
    con = None
    try:
        con = connect('item.db')
        cs = con.cursor()
        cs.execute(itemsql.ITEM_DELETE % datas)
        con.commit()
    except:
        raise Exception
    finally:
        close(cs, con)


def update(*datas):
    cs = None
    con = None
    try:
        con = connect('item.db')
        cs = con.cursor()
        cs.execute(itemsql.ITEM_UPDATE % datas)
        con.commit()
    except:
        raise Exception
    finally:
        close(cs, con)


def selectone(*ids):
    cs = None
    con = None
    try:
        con = connect('item.db')
        cs = con.cursor()
        result = cs.fetchall()
        cs.execute(itemsql.ITEM_SLETE_ONE % ids)
        datas = cs.fetchall()
        for i in datas:
            print(i)
    except:
        raise Exception
    finally:
        close(cs, con)
    return result


def select():
    cs = None
    con = None
    try:
        con = connect('item.db')
        cs = con.cursor()
        cs.execute(itemsql.ITEM_SELETE)
        result = cs.fetchall()
    except:
        raise Exception
    finally:
        close(cs, con)
    return result


def selects():
    cs = None
    con = None
    try:
        con = connect('item.db')
        cs = con.cursor()
        cs.execute(itemsql.ITEM_SELETES)
        result = cs.fetchall()
    except:
        raise Exception
    finally:
        close(cs, con)
    return result


def select_ui():
    cs = None
    con = None
    lists = []
    try:
        con = connect('item.db')
        cs = con.cursor()
        cs.execute(itemsql.ITEM_SELETE)
        results = cs.fetchall()
        # [(),(),()]
        for res in results:
            st = '%d,%s,%d,%f'
            lists.append(st % res)
    except:
        raise Exception
    finally:
        close(cs, con)
    return lists


if __name__ == '__main__':

    try:
        result = select_ui()
        print(result)
    except:
        print('error')
        raise

    # makeTable #
    # makeTable('item.db')

    # insert #
    # try:
    #     insert(106, 'pants', 10000, 3.4)
    # except:
    #     print('Error')

    # select #

    # update #
    # try:
    #     update('pant', 125, 100050, 3.24)
    # except:
    # #     print('Error')

    # delete #
    # try:
    #     delete(125)
    # except:
    #     print('Error')

    # selectone #
    # try:
    #     results = selectone(104)
    # except:
    #     raise Exception

