# 랜덤수를 이용해서 주사위를 굴리고 3이 나오면 프로그램을 종료할 수 있도록 작성
# while 문을 이용해서 3이 나오기 전까지 주사위를 계속 굴릴 수 있도록 작성

import random
while True:
    num = random.randint(1, 6)
    print(num)
    if num == 3:
        break

print("*"*30)
count = 0
num = 0
while num != 3:
    num = random.randint(1, 6)
    count = count + 1
    print(num)

print("*"*30)
print("실행횟수 : {}".format(count))
print("end")
