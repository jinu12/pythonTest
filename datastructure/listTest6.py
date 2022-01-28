# 리스트를 제어할 수 있는 함수 사용하기
list1 = list(range(0, 51, 5))
list1.append(20)
print(list1)
print(list1.count(20))

print(list1.index(45))

# pop : 리스트의 맨 뒤의 항목을 빼서 리턴하며 리스트에서 항목을 지운다.
myelement = list1.pop()
print(myelement)
print(list1)

list1.insert(2, 77)
print(list1)

list1.remove(5)
print(list1)

list1.sort()
print(list1)

list1.sort(reverse=True)
print(list1)

examlist = []
while True:
    num = int(input("1. 추가 2. 제거 3. 조회 4.종료\n입력 : "))
    if num == 1:
        addNum = int(input("몇 번 추가 할 건지 입력해주세요 : "))
        for i in range(addNum):
            examlist.append(int(input("숫자를 입력해주세요 : ")))
        print("")
    elif num == 2:
        examlist.remove(int(input("제거할 숫자를 입력해주세요 : ")))
    elif num == 3:
        for i in range(len(examlist)):
            print(examlist[i], end=" ")
        print("")
    elif num == 4:
        break
    else:
        print("정확한 숫자를 입력해주세요.")
