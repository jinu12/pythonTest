# 문자열의 인덱싱과 슬라이싱
str1 = "python programming"
print(str1)
print("문자열의길이:", len(str1))
print(str1[0])
print(str1[-1])
print(str1[0:5])
print(str1[:5])
print(str1[5:])
print(str1[:])
print(str1[::-1])

# 문자열 하나씩 엑세스
for i in str1:
    print("{} {}".format(i, type(i)))
    if i == "p":
        print("결과보기")
    else:
        print("테스트완료")

for i in range(len(str1)):
    print(str1[i], end="")