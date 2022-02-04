# 3단을 출력하는 함수를 정의학 호출해서 사용하세요.
print("*" * 60)

print("3단")


def printGugu():
    for i in range(1, 10):
        print("{} * {} = {}".format(3, i, 3 * i))


printGugu()

print("*" * 60)

# 1부터  100까지의 합을 출력하는 합수를 만들어 보세용


def printSum():
    total = 0
    for i in range(1, 101):
        total = total + i
    print("1부터 100까지 합 => ", total)


printSum()

print("*" * 60)
