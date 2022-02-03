# 튜플의 생선방법
tuple1 = (10, 20, 30)
print(tuple1)
print(type(tuple1))

list1 = [1, 2, 3, 4]
print(list1, ":", type(list1))
print(tuple(list1), ":", type(tuple(list1)))

tuple2 = 40, 50, 60
print(tuple2)
print(type(tuple2))

# 튜플에 저장될 요소가 한 개인 경우 아래와 같이 사용하면 int형 데이터로 인식
# 튜플로 인식할면 뒤에 ,(콤마)를 추가
tuple3 = (10)
print(tuple3)
print(type(tuple3))

tuple4 = (10, )
print(tuple4)
print(type(tuple4))

# 빈 튜플을 만드는 방법
tuple5 = ()
print(tuple5)
print(type(tuple5))

tuple6 = tuple()
print(tuple6)
print(type(tuple6))

# 튜플도 range함수를 이용해서 만들 수 있다.
tuple7 = tuple(range(10))
print(tuple7)
print(type(tuple7))