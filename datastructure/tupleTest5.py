# 튶르이 변환
# 튜플 -> 리스트 -> 튜플
tuple1 = (10, 20, 30)
print(type(tuple1))
print(tuple1)

list1 = list(tuple1)
print(type(list1))
print(list1)

list1.append(188)
print(list1)

tuple1 = tuple(list1)
print(type(tuple1))
print(tuple1)

# 리스트나 튜플의 값을 거내서 여러 개의  변수에 한꺼번에 담는 작업만 가능 - 언팩킹
num1, num2, num3 = (10, 20, 30)
print(" {}, {], {}".format(num1, num2, num3))

num4, num5, num6 = [10, 20, 30]
print(" {}, {}, {}".format(num4, num5, num6))

list2 = [100, 200, 300]
tuple2 = [400, 500, 600]
value1, value2, value3 = list2
print("{} . {}. {}".format(value1, value2, value3))

value1, value2, value3 = tuple2
print("{}, {}, {}".format(value1, value2, value3))