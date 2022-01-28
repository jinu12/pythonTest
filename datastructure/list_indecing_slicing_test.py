# 리스트의 인덱싱
list1 = list(range(10, 101, 10))
print(list1)

print(list1[1])
print(list1[5])
print(list1[9])
print(list1[-1])
print(list1[-5])

# 리스트의 슬라이싱
print(list1[4:10:1])
print(list1[4:10:2])
print(list1[4:10])
print(list1[:2])
print(list1[2:])

'''
    리스트 인덱싱
        리스트에 저장된 자료의 위치를 참조해서 활용할 수 있다.
        리스트, 튜플, 문자열등은 한 요소식 인덱스를 가지고 0부터 접근할 수 있다
        역순으로 접근이 간으하다.
        리스트, 튜플, 문자열등은 리스트명으로 접근이 가능하다는 으미
        음수 값으로 접근이 가능 
    
    리스트의 슬라이싱
        특정 구간의 자료를 리턴할 수 있도록 기능을 제공
'''
