# 이차원리스트의 생성과 사용방법
# 중첩된 것과 동일한 개념으로 이중 for문을 이용해서 작업
list1 = [
    [1, 2],
    [3, 4, 5],
    [6, 7, 8, 9]
]

print(list1[0])
print(list1[2][3])

for row in list1:
    for i in row:
        print(i, end=" ")
    print("")

print("*" * 60)

list2 = [
    [1, [11, 12]],
    [3, 4, [55, 56],
     [6, 7, 8, 9]]
]

for i in list2:
    for j in i:
        for k in j:
            print(k, end=" ")
    print("")

print("*" * 60)
