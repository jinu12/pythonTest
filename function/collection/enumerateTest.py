# 리스트의 index와 값을 tuple로 만들어 리턴하는 함수
list1 = list(range(1, 10, 2))
print(list1)
print(enumerate(list1))
print(tuple(enumerate(list1)))

for index, value in enumerate(list1):
    print("{} : {}".format(index, value))
print("*" * 30)

for index, value in enumerate(list1, start=1):
    print("{} : {}".format(index, value))
