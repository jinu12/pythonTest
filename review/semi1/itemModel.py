

class Item:
    def __init__(self, ids, name, price, rate):
        self.__ids = ids
        self.__name = name
        self.__price = price
        self.__rate = rate

    def __str__(self):
        return str(id) + ' ' + self.__name + ' ' + str(self.__rate)

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
        self.__ids = price

    def getRate(self):
        return self.__ids

    def setRate(self, rate):
        self.__ids = rate
