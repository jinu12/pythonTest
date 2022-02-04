# add 함수
# 두 수를 입력 받아서 더한 결과를 리턴하도록 구현
# num = int(input("첫번째 숫자 : "))
# num2 = int(input("두번째 숫자 숫자 : "))

def printAdd(num, num2):
    total = num + num2

    return total


# printSumAvg함수

def printSumAvg(num, num2, num3):
    total = num + num2 + num3
    avg = (num + num2 + num3) / 3
    print("총합 : ", total)
    print("평균 : ", avg)


# multiply 함수

def multiply(num, num2):
    multiplys = num * num2

    return multiplys


# 함수 호출
first = int(input("첫번째 숫자 : "))
second = int(input("두번째 숫자 숫자 : "))

print("총합 :", printAdd(first, second))

hana = int(input("첫번째 숫자 : "))
duo = int(input("두번째 숫자 숫자 : "))
tet = int(input("두번째 숫자 숫자 : "))

printSumAvg(hana, duo, tet)

one = int(input("첫번째 숫자 : "))
two = int(input("두번째 숫자 숫자 : "))

print("곱 =>", multiply(one, two))
