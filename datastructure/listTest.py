# 자료구조
# - 데이터를 저장하기 위해 제공되는 구조
# - 파이썬의 자료구조는 기스트, 튜플, 딕셔너리, 집합이 있다
# - 리스트와 튜플은 데이터에 순서가 있다.
# - 자료구조와 저장된 자료의 순서를 찾을 수 있고 접근할 수 잇다.(인덱싱)
# - 전체 자료를 부분적으로 잘라서 접근할 수 있다. (슬라이싱)

# 리스트 []
# - 순서가 있는 자료구조
# - 인덱싱과 슬라이싱이 가능
# - 저장된 데이터의 수정이 가능
# - 리스트안에 문자열, 정수, 다양한 형태의 데이터를 저장할 수 있다.
# - index 로 접근
# - index는 0부터 시작

# 튜플 ()
# - 순서가 있는 데이터 구조
# - 인덱싱과 슬라이싱이 가능
# - 저장된 데이터의 수정이 불가능

# dictionary
# - 키와 value 한쌍으로 데이터 저장
# - 순서를 가지고 있지 않다.
# - 인덱싱과 슬라이싱이 불가능

num1 = 100
num2 = 95
num3 = 50
num4 = 100
num5 = 45

subject1 = "python"
subject2 = "javascirpt"
subject3 = "android"
subject4 = "raspperjPi"
subject5 = "mqtt"

jumsulists = [num1, num2, num3, num4, num5]
subjectLists = [subject1, subject2, subject3, subject4, subject5]

print(jumsulists)
print(subjectLists)

print(jumsulists[0])
print(jumsulists[1])

print("타입=", type(jumsulists))
print("타입=", type(subjectLists))

for i in subjectLists:
    print(i, end=" ")
print("")


print("*" * 40)

for j in subjectLists:
    print(j)
    for i in jumsulists:
        print(i)

print("*" * 40)

for j in subjectLists:
    print(j + " : ", end="")
    for i in jumsulists:
        print(i, end=" ")
    print("")
