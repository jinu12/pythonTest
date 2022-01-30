# 초기값, 마지막 값, 증가값 입력 받아서 값들의 총합 작성하는 프로그램
Sum = 0
earlyInput = int(input("초기값을 정수로 입력하세요.:"))
inputNum = int(input("마지막값을 정수로 입력하세요.:"))
plusNum = int(input("증가분을 정수로 입력하세요.:"))
for i in range(earlyInput, inputNum+1, plusNum):
    Sum = Sum + i
print("총합은 {}입니다".format(Sum))