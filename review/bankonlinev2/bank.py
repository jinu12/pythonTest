from account import Account

# acc1 Object
acc1 = Account('11112222', 1000, 'James')
try:
    acc1.withdraw(900)
    print(acc1)
except:
    print('잔액부족')
    raise

# name change
acc1.setowner('Kim')
print(acc1)

# account number, customer name print
print(' 계좌 : %s , 이름 : %s' % (acc1.accno, acc1.owner))
