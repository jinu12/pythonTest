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
        if balance <= 0:
            self.__balance = 0
        else:
            self.__balance = balance
        # self.__balance = balance
        self.__owner = owner

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, owner):
        self.__owner = owner

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

# IAccount
# 1. 속성 : accno, balance, name, interest
# 2. 행위 : deposit, withdraw, inquire, calcinerest

# Inheritance(상속)


class IAccount(Account):
    def __init__(self, accno, balance, name, interest):
        super().__init__(accno, balance, name)
        self.__interest = interest

    def __str___(self):
        return super().__str__() + '' + str(self.__interest)

    def calcinterest(self):
        return super().inquire() * (self.__interest / 100)

    def getInterest(self):
        return self.__interest

    def setInterest(self, interest):
        self.__interest = interest

