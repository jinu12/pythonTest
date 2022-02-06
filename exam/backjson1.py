# 파보나치 수열
num = int(input("파보나치 수열의 갯수를 입력해주세요:"))


def fabonachi():
    pabo = 0
    if num == 1:
        pabo = 1
    if num == 2:
        pabo = 1
    elif num >= 3:
        for i in range(1, num-1):
            pabo = i + i
    print("파보나치 수 : ", pabo)


fabonachi()
