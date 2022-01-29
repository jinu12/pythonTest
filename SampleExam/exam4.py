while True:
    num = int(input("1보다 크고 10보다 작은 정수를 입력하시오. : "))
    if num < 1 or num > 10:
        print("잘못된 숫자가 입력되었습니다.")
        break
    for i in range(num):
        for j in range(1, 10, 1):
            print("{} * {} = {}".format(num, j, num * j))
        print("")