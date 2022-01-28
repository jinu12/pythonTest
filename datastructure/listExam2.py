"""
1. 리스트에 요소의 갯수를 입력 받고 각 요소에 저장될 값들을 입력받아 리스트를 작성하세요
    리스트의 요소를 몇 개 만들까요? _______5
    리스트에 추가될 값을 입력해주세요 : ______
    리스트에 추가될 값을 입력해주세요 : ______
    리스트에 추가될 값을 입력해주세요 : ______
    리스트에 추가될 값을 입력해주세요 : ______
    리스트에 추가될 값을 입력해주세요 : ______

2. 1번에서 작성된 리스트의 요소를 0번부터 출력, n-1 번부터 출력
   range를 활용해서 작업하기
   [10,20,30,40,50]

3. 2번에서 출력한 요소의 평균합, 총합 구하기
   요소의 평균: ______
   요소의 합 : ______
"""
elementList = []
printelement = ""
Sum = 0
num = int(input("리스트의 요소를 몇 개 만들까요?"))
for i in range(num):
    element = int(input("리스트에 추가될 값을 입력하세요 : "))
    elementList.append(element)

for i in range(len(elementList)):
    Sum = Sum + elementList[i]
    print("{} ".format(elementList[i]), end="")
print("")

for i in range(len(elementList)-1, -1, -1):
    print("{} ".format(elementList[i]), sep=",", end="")
print("")

avg = Sum / len(elementList)
print("요소의 합 : {}".format(Sum))
print("요소의 평균 : {}".format(avg))
