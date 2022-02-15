# ws03.py
#
# 3. Number Guess 게임 구현
#
# 1) 게임 진행 카운트를 출력 한다.
import random


def exits():
    print('계속하시겠습니까 계속 1 종료 2')
    accessnum = int(input())
    if accessnum == 1:
        start()
    elif accessnum == 2:
        finish()
    else:
        print('보기에 해당하는 숫자를 입력해주세요')


def finish():
    exit()


def start():

    count = 0
    num = random.choice(range(1, 101))
    while True:
        inputnum = int(input('생각한 숫자를 입력해주세요.'))
        count = count + 1
        print('게임 횟수 :', count)
        print(num)
        # 2) 5회가 되면 게임 Fail !
        if count == 5:
            print("Fail !")
            # 게임이 종료 되면 다시 게임을 시작 할 수 있게 하기
            exits()

        # 3) 입력한 숫자가 큰지 작은지 출력
        if num < inputnum:
            print('입력된 숫자가 큽니다')
        elif num > inputnum:
            print('입력된 숫자가 작습니다')
        else:
            print("Correct")
            exits()


if __name__ == '__main__':
    start()
