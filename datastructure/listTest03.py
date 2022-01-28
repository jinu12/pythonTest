# 리스트를 만들고 엑세스하는 방법
list1 = list(range(1, 20, 2))
# start, and, stop
print(list1)

# 리스트에서 사용할 수 있는 기능
# reversed함수를 이욯해서 range로 생성한 리스트를 reverse시킬 수 있다.
list2 = list(reversed(range(1, 20, 2)))

Str = list('python programming')
print(Str)

for i in Str:
    print(i, end="")
print("")

print("*" * 60)

print(len(Str))

for i in range(len(Str)):
    print("{}:{}".format(i, Str[i]), end=" ")
print("")

print("*" * 60)

for i in range(len(Str)-1, -1, -1):
    print("{}:{}".format(i, Str[i]), end=" ")
print("")

print("*" * 60)

ReStr = list(reversed(Str))

for i in ReStr:
    print(i, end="")
print("")
print("*" * 60)
