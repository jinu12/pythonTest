balance = 0


def deposit(money):
    global balance
    balance += money


def inquire():
    return balance


def deposit2(money):
    global balance
    balance += money


def inquire2():
    return balance


result = inquire()
print(result)
deposit(10000)
result = inquire()
print(result)

result2 = inquire2()
print(result2)
print(20000)
result2 = inquire2()
print(result2)