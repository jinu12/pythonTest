# 랜덤과 리스트를 이요하여 로또번호 발생하고 저장하여 출력
import random

print("랜덤번호")
randomlist = []
for i in range(6):
    randomlist.append(random.choice(range(1, 46)))
    if i != 5:
        print("{}".format(randomlist[i]), end=", ")
    else :
        print("마지막 숫자는 {}".format(randomlist[i]))


