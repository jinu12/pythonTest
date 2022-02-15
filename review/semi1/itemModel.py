import itemsql


class Item:
    def __init__(self, ids, name, price, rate):
        self.__ids = ids
        self.__name = name
        self.__price = price
        self.__rate = rate

    def getId(self):
        return self.__ids

    def setId(self, ids):
        self.__ids = ids

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getPrice(self):
        return self.__price

    def setPrice(self, price):
        self.__price = price

    def getRate(self):
        return self.__rate

    def setRate(self, rate):
        self.__rate = rate

    def getUpdate(self):
        return itemsql.ITEM_UPDATE % (self.__name, self.__price, self.__rate, self.__ids)

    def getInsert(self):
        return itemsql.ITEM_INSERT % (self.__ids, self.__name, self.__price, self.__rate)

    def __str__(self):
        return str(id) + ' ' + self.__name + ' ' + str(self.__rate)
