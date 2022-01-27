# 출력할 단을 입력받아 입력된 구구단을 출력할 수 있도록 작성 출력형태
# num = int(input("단 : "))
# for i in range(1, 10):
#     print("%d * %d = %d" % (num, i, num * i))


for i in range(2, 9):
    print("{} 단".format(i))
    for j in range(1, 9):
        print("{} * {} = {}\t".format(i, j, (i * j)), end=" ")
    print(" ")

print("*"*40)

for i in range(2, 9):
    print("{} 단".format(i))
    for j in range(1, 9):
        print("{} * {} = {}".format(i, j, (i * j)))
    print("", end="")
