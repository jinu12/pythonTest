#  음수를 입력하면 중단하는 프로그램
countList = []
examList = [1, 2, 3, 4, 5]
count = -1
print("입력:")
while True:
    num = int(input(""))
    countList.append(num)
    count = count + 1
    if num < 0:
        print(countList[count-1])
        break
