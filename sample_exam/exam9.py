# 두 수의 최대 공약수 구하기
commonList = []


def gcd(num1=int(input("숫자를 입력해주세요 : ")), num2=int(input("숫자를 입력해주세요 : "))):
    if num1 < num2:
        for i in range(1, num2 + 1):
            if num1 % i == 0 and num2 % i == 0:
                commonList.append(i)
    else:
        for i in range(1, num1 + 1):
            if num1 % i == 0 and num2 % i == 0:
                commonList.append(i)

    for i in range(len(commonList)):
        return commonList[i]


print(gcd())
