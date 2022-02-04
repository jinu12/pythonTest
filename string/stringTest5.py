# 문자열 나누기 합치기
str1 = "python은 정말 재밌다."
str2 = "java:python:C$:C++"

result1 = str1.strip(" ")
print("결과=>", result1)
print(type(result1))

result2 = str2.split(":")
print("결과=>", result2)
print(type(result2))

list1 = ['java', 'python', 'C#', 'C++']
str3 = " ".join(list1)
print("결과=>", str3)

