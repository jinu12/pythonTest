from account import IAccount

# acc1 Object
iacc1 = IAccount('11112222', 1000, 'James', 3.4)
try:
    iacc1.withdraw(900)
    print(iacc1)
except:
    print('잔액부족')
    raise

interest = iacc1.calcinterest()
print(interest)
print(iacc1.accno + ' ' + iacc1.owner + iacc1.getInterest())
