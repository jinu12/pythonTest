# Account

# Class
# 1. 속성
# 2. 행위

# Account Class
# 1. 속성 : balance
# 2. 행위 : deposit, widthdraw

class Account:
    # Constructor(생성자))
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, money):
        self.balance += money

    def withdraw(self, money):
        self.balance -= money

    def inquire(self):
        return self.balance

    def __str__(self):
        return self.balance
