# 튜플은 인덱싱과 슬라이싱이 가능
tuple1 = tuple(range(10))
print(tuple1)

# 각 요소를 접근하는 경우 리스트와 동일하게 [을 통해 접근한다.
print(tuple1[0])
print(tuple1[-1])
print(len(tuple1))
print(tuple1[len(tuple1)-1])
print(tuple1[1:3])
print(tuple1[5:])
print(tuple1[:len(tuple1)])
