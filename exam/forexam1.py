num = int(input("단 : "))
i = 1
while i < 10:
    print("%d * %d = %d" % (num, i, num * i))
    i = i + 1

print("############################")

num = 1
while True:
    if num >= 10:
        break
    print("무한루프")
    num = num + 1
