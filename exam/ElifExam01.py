test = bool
while test:
    case = input('점수 확인 확인 : 1, 종료 : 2\n')
    if case == "1":
        jumsu = int(input(" 점수 : "))
        if 0 < jumsu < 100:
            if jumsu >= 90:
                print('수')
            elif jumsu >= 80:
                print('우')
            elif jumsu >= 70:
                print('미')
            elif jumsu >= 60:
                print('양')
            else:
                print('가')
        else:
            print('잘못입력')
    if case == "2":
        print('종료되었습니다.')
        test = False
