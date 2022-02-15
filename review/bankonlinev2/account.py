# Account

# Class
# 1. 속성
# 2. 행위

# Account Class
# 1. 속성 : balance
# 2. 행위 : deposit, widthdraw

class Account:
    # Constructor(생성자))
    def __init__(self, accno, balance, owner):
        self.__accno = accno
        self.__balance = balance
        self.__owner = owner

    def setowner(self, owner):
        self.__owner = owner

    @property
    def owner(self):
        return self.__owner

    @property
    def accno(self):
        return self.__accno

    def getaccno(self):
        return self.__accno

    def deposit(self, money):
        self.__balance += money

    def withdraw(self, money):
        if (money <= 0) or (money > self.__balance):
            return
        self.__balance -= money

    def inquire(self):
        return self.__balance

    def __str__(self):
        return self.__accno + ":" + str(self.__balance) + ":" + str(self.__owner)
