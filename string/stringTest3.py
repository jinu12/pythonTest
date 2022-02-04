# 문자열관련함수 = count, index, find
str1 = "Python P"
result = str1.count("P")
print(result, "개의 문자가 반복 출력됨")

# index() vs find()
# 문자열내에 지정한 문자가 존재하는 경우 동일한 결과
print(str1.index("y"), "빈 위치")
print(str1.find("y"), " 빈 위치")
# 문자열내에 지정한 문자가 존재하지 않는 이유
print(str1.find("j"), " 빈 위치")
# 찾는 문자가 없는 경우 -1을 리턴
# print(str1.index("j"), " 빈 위치")
# 찾는 ㅁ문자가 없는 경우 에러를 발생


# 해당 문자열로 시작, 종료하는지 확인(True or False를 리턴
str2 = "python programming"
if str2.startswith("py"):
    print("Ok")
else:
    print("Fail")

if str2.endswith("ing"):
    print("Ok")
else:
    print("Fail")
