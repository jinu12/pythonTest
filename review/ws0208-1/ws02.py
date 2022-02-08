# 3개의 숫자를 입력 받아서
while True:
    maxnum = 0
    minnum = 0
    print('두자리 자연수 3개를 입력해주세요.')
    num1 = int(input('숫자를 입력해주세요:'))
    num2 = int(input('숫자를 입력해주세요:'))
    num3 = int(input('숫자를 입력해주세요:'))
    # 단, 숫자는 두자리 숫자를 입력 받아야 하며 양수를 입력 받아야 한다.
    if not num1 > 10:
        # 이외의 숫자가 입력 될때는 프로그램 종료 한다.
        print('프로그램을 종료합니다')
        break
    elif num2 < 10:
        # 이외의 숫자가 입력 될때는 프로그램 종료 한다.
        print('프로그램을 종료합니다')
        break
    elif num3 < 10:
        # 이외의 숫자가 입력 될때는 프로그램 종료 한다.
        print('프로그램을 종료합니다')
        break

    numslist = list()
    numslist.append(num1)
    numslist.append(num2)
    numslist.append(num3)

    print('최대값 최소값의 차이 :', max(numslist) - min(numslist))


