# map (function, 자료구조)
# => 두 번째 매개변수로 정의한 자료구조만의 모든 데이터를 꺼내서 첫 번째 매개변수에 정의한
# function을 적용해서 리턴

list1 = [10.123, 34.56, 55.18, 99.789]
# 위의 리스트에 지정된 데이터를 int로 벼놘해서 저장할 수 있도록 처리하세요
for index, value in enumerate(list1):
    list1[index] = int(value)
print(list1)

# map 함수 사용
list2 = list(map(int, list1))
print(list2)

list3 = ["test", "python programming", "list", "tuple"]
# List3의 각요소의 문자열의 길이를 출력
print(tuple(map(len, list3)))
