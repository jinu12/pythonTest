# 출력할 단을 입력받아 입력된 구구단을 출력할 수 있도록 작성 출력형태
num = int(input("단 : "))
for i in range(1, 10):
    print("%d * %d = %d" % (num, i, num * i))
