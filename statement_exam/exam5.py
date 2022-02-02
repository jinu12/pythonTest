# 길이가 10인 리스트 원본과 랜범 번호
import random

tenlist = list(range(1, 11, 1))
print("원본 :", end="")
for i in range(len(tenlist)):
    print("{},".format(i), end="")

print("")

print("결과 :", end="")
for i in range(len(tenlist)):
    print("{},".format(random.randrange(len(tenlist))), end="")
