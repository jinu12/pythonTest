import random


def lottoprocess(lotto_nums, user_nums):
    totalmoeny = '총 담첨 금액 : '
    selectmoney = '담첨 금액 : '
    bonus = lotto_num[6]
    money = random.choice(range(1000000000, 10000000000))

    print(totalmoeny + format(int(money), ','))
    print("=" * 70)

    collect_num = []  # 맞춘 리스트 초기화

    count = 0  # 맞은 갯수 초기화

    for n in range(0, 6):  # count 변수를 통해 구매번호와 당첨번호 리스트 내부의 변수가 같은지 판별하여, 같으면 count 숫자를 하나씩 올린다.
        for k in range(0, 6):
            if lotto_nums[n] == user_nums[k]:
                collect_num.append(lotto_num[n])
                count = count + 1

    if count == 6:
        print("1등 담첨이 되었습니다.")
        print(selectmoney + str(money * 0.5))

    elif count == 5:  # 5개가 같고, 보너스 숫자가 들어 있다면 2등
        if user_num.count(bonus) == 1:
            print("맞은 숫자는 {} 맞춘 갯수 {}개, 보너스 숫자는 {} 2등에 담청되었습니다..".format(sorted(collect_num), count, bonus[0]))
            print(selectmoney + str(money * 0.3))
        else:
            print("맞은 숫자는 {} 맞춘 갯수 {}개, 보너스 숫자는 {} 3등에 담청되었습니다..".format(sorted(collect_num), count, bonus[0]))
            print(selectmoney + str(money * 0.1))

    elif count == 4:
        print("맞은 숫자는 {} 맞춘 갯수 {}개, 4등에 담청되었습니다".format(sorted(collect_num), count))
        print(selectmoney + str(money * 0.005))

    elif count == 3:
        print("맞은 숫자는 {} 맞춘 갯수 {}개, 5등에 담청되었습니다..".format(sorted(collect_num), count))
        print(selectmoney + str(money * 0.0000001))

    else:
        if count == 0:
            print("맞은 숫자는 횟수가 없어서 담첨 되지 않았습니다.")
            print(selectmoney + "0")
        else:
            print("맞춘 갯수 {}개, 담첨 되지 않았습니다.".format(count))
            print(selectmoney + "0")


lotto_num = [1, 2, 3, 4, 5, 6, 7]
user_num = [1, 2, 3, 4, 5, 6]
lottoprocess(lotto_num, user_num)