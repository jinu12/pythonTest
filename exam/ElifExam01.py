"""
    jumsu 변수에 입력받은 값을 저장하여 수우미양가를 출력
    90~100 : 수 , 80~89 : 우 , 70~79 : 미 , 60~69 : 양  , 0~59 : 가
    단, 0보다 작거나 100 초과된 점수를 입력하면 "잘못입력" 출력
"""

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
