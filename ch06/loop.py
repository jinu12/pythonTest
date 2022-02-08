# 1~ 10까지의 합을 구하시오
# for 문
import random
#
# total = 0
# for i in range(1, 11):
#     total = total + i
# print("총합: ", total)
# while 문
# total2 = 0
# i = 0
# while i < 11:
#     total2 = total2 + i
#     i = i + 1
# print("총합: ", total2)
#
import time

while True:
    temp = random.randint(1, 11)
    print(temp)
    if temp == 5:
        break
    time.sleep(3)

# 파이썬 로또 프로그램 짜기


def lottoProgram():
    user_num = []
    collect_num = []
    count = 0
    while True:
        select = int(input("수동으로 하시겠습니까? 자동으로 하시겠습니까? 1: 자동, 2: 수동"))
        if select == 1:
            print("로또 자동으로 구매합니다.")
            user_num = random.sample(range(1, 46), 6)
            print("사용자 구매 번호", sorted(user_num))
        elif select == 2:
            print("로또 수동으로 구매합니다.")
            for i in range(0, 6):
                user_num.append(int(input()))
            print("사용자 구매 번호", sorted(user_num))
        print("로또 구매 시간이 지났습니다.")
        print("담청자를 조회합니다.")
        lotto_num = random.sample(range(1, 46), 7)
        bonus = [lotto_num[6]]
        print("로또 번호", sorted(lotto_num[:6]))
        print("보너스 로또 번호 : ", bonus[0])
        for n in range(0, 6):
            for k in range(0, 6):
                if lotto_num[n] == user_num[k]:
                    collect_num.append(lotto_num[n])
                    count = count + 1
        if count == 6:
            print("1등 담첨이 되었습니다.")
            break
        elif count == 5:
            if user_num.count(bonus[0]) == 1:
                print("2등 담첨이 되었습니다.")
            else:
                print("3등 담청이 되었습니다.")
            break
        else:
            if count == 0:
                print("맞은 숫자는 횟수가 없어서 담첨 되지 않았습니다.".format(collect_num[:], count), end=" ")
            else:
                print("맞은 숫자는 {} 횟수는 {} 담첨 되지 않았습니다.".format(collect_num[:], count), end=" ")
            break


lottoProgram()
