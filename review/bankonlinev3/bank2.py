from account import Account

accs = list()
accs.append(Account('111', 1000, 'lee'))
accs.append(Account('222', 2000, 'kim'))
accs.append(Account('333', 3000, 'han'))

for ac in accs:
    print('계좌번호 : %s, 계좌주: %s, 잔액 %d' % (ac.accno, ac.owner, ac.inquire()))
