# 컴퓨터가 생성한 숫자 맞추기 -랜덤수를 활용
import random

answer = 0
count = 0
num = random.randrange(1, 101)
while True:
    count = count + 1
    answer = int(input("1~100 까지의 숫자를 입력해주세요 : "))
    if answer < num:
        print("사용자가 입력한 숫자가 랜덤수보다 작습니다 다시 입력해주세요.")
    elif answer > num:
        print("사용자가 입력한 숫자가 랜덤수보다 큽니다 다시 입력해주세요.")
    else:
        print("정답입니다.")
        break

print("랜던수 : {} , 사용자가 입력된 숫자 : {}, 실행횟수 : {}".format(num, answer, count))

# import random
#
# answer = 0
# num = 0
# while True:
#     num = random.randrange(1, 101)
#     answer = int(input("1~100 까지의 숫자를 입력해주세요 : "))
#     print("랜덤 수: ", num)
#     print("사용자 수: ", answer)
#     if answer < num:
#         print("사용자가 입력한 숫자가 랜덤수보다 작습니다 다시 입력해주세요.")
#     elif answer > num:
#         print("사용자가 입력한 숫자가 랜덤수보다 큽니다 다시 입력해주세요.")
#     else:
#         print("정답입니다.")
#         break

