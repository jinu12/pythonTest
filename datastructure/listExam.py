# 88, 99, 77. 100, 99의 점수를 저장할 수 있는 리스트를 작성한 후 점수의 총합과 평균을 계산해서 출력하세요
# [출력 형태]
# 점수 총합 :
# 평균 :
import random

List = [88, 99, 77, 100, 99]
Sum = 0

for i in List:
    Sum = Sum + i
avg = Sum / len(List)
print("점수 총합 : ", Sum)
print("평균 : ", avg)

# Lists = []
# while True:
#     num = input("조회할려면 1, 점수를 추가할려면 2, 죵료할려면 3 ")
#     if num == "1":
#         for i in Lists:
#             print(i)
#     elif num == "2":
#         jumsu = int(input("점수를 입력해주세요 : "))
#         Lists.append(jumsu)
#     elif num == "3":
#         break
#     else:
#         print("정확한 숫자를 입력해주세요")

Str = "python programming"

Lists = []
for i in range(0, 18):
    Lists.append(Str[i])
print(Lists)

PythonList = ""

for i in range(0, 18):
    PythonList = PythonList + Lists[i]
print(PythonList)

print("*" * 40)

changePythonList = ""

for i in range(17, -1, -1):
    changePythonList = changePythonList + Lists[i]
print(changePythonList)
print("*" * 40)


#
# StrList.sort(reverse=True)
# for i in StrList:
#     print(i)

num = 10
print(random.randrange(1, num+1))
print(random.randint(1, num))

Str = list('python programming')
print(Str)

for i in Str:
    print(i, end="")
print("")

print("*" * 60)

print(len(Str))

for i in range(len(Str)):
    print("{}: {}".format(i, Str[i]), end=" ")
print("")

print("*" * 60)

for i in range(len(Str)-1, -1, -1):
    print("{}: {}".format(i, Str[i]), end=" ")
print("")

print("*" * 60)

ReStr = list(reversed(Str))

for i in ReStr:
    print(i, end="")
print("")
print("*" * 60)
