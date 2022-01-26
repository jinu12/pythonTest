# 미션
# 숫자를 입력 받아 양수, 음수, 0을 출력할 수 있도록 작성
# 출력 형식
"""
    숫자1 : 10
    입력한 숫자는 10이며 양수입니다.

    숫자2 : -10
    입력한 숫자는 10이며 음수입니다.

    숫자1 : 0
    입력한 숫자는 0이며 제로입니다.
"""
'''
test = bool
while test:
    case = input('숫자 입력 확인 : 1, 종료 : 2\n')
    if case == "1":
        num = int(input(" 숫자 1 : "))
        if num > 0:
            print('입력한 숫자는 %d 이며 양수입니다.' % num)
        elif num < 0:
            print('입력한 숫자는 %d 이며 음수입니다.' % num)
        else:
            print('입력한 숫자는 %d 이며 제로입니다.' % num)
    if case == "2":
        print('종료되었습니다.')
        test = False
'''
test = bool
while test:
    case = input('숫자 입력 확인 : 1, 종료 : 2\n')
    if case == "1":
        num = int(input(" 숫자 1 : "))
        result = ""
        if num > 0:
            result = "양수"
        elif num < 0:
            result = "음수"
        else:
            result = "제로"
        print("입력한 숫자는 %d 이며 %s입니다" % (num, result))
    if case == "2":
        print('종료되었습니다.')
        test = False

