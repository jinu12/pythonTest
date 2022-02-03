# 집합과 리스트의 차이점
# => 리스트는 중복이 가능하지만 집합은 중복이 불가능
set1 = {"java", "python", "C++", "kotlin","kotlin"}
list1 = ["java", "python", "C++", "kotlin", "kotlin"]
print(list1)
print(set1)

# 빈집합 생성
# set2 = {} {}로 정의하면 딕셔너리로 인식
set2 = set()
print(type(set2))

# set의 데이터 추정
set2.add("java")
set2.add("python")
print(set2)

set1.remove("kotlin")
print(set1)

set1.update(set2)
# 합집합의 의미
print(set1)