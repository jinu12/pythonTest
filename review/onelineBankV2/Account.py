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
        self.accno = accno
        self.balance = balance
        self.owner = owner

    def deposit(self, money):
        self.balance += money

    def withdraw(self, money):
        self.balance -= money

    def inquire(self):
        return self.balance

    def __str__(self):
        return self.accno + ":" + str(self.balance) + ":" + str(self.owner)
