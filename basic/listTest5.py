# 리스트의 연산과 리스트의 값 변겨아기
list1 = list(range(0, 101, 10))
print(list1)

list1[2] = 70
print(list1)

list1[2:4] = [200, 300]
print(list1)

list1[len(list1) - 1] = [1000, 2000]
print(list1)

print(list1[1])
print(list1[1][2])

del(list1[0])
print(list1)

del(list1[2:4])
print(list1)

list1[2:4] = []
print(list1)

# del(list1)
# print(list1)

'''
    리스트의 값을 변경
        index를 이용해서 지정한 위치의 요소값을 병경할 수 있다
        리스트[index] = 변경할 값
            _________  _________
    슬라이싱을 적용 가능 여러 개 값으로 수정, 새로운 리스트를 추가 적용 가능
    
'''