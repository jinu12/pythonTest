# 문자열ㅇ의 구성을 체크하는 함수 : isXXXX (True or False를 리턴)
str1 = "12345"
str2 = "12345ffddds"
str3 = "test"
str4 = "테스트"
str5 = "test123"
str6 = "Test"
print(str1.isdigit())
print(str2.isdigit())
# 숫자?
print(str3.isalpha())
print(str4.isalpha())
# 문자?
print(str5.isalnum())
# 숫자문자?
print(str6.isupper())
# 대문자
print(str3.islower())
# 소문자
print(" ".isspace())
# 공백
