# 표준입력
num1 = int(input("숫자 1 : "))
num2 = int(input("숫자 2 : "))

# 표준출력
print("입력 숫자 1 : ", num1)
print("입력 숫자 2 : ", num2)

print(num1, num2)
print(num1, num2, sep=', ')
# sep = 구분자를 포함해서 출력

print("%d / %d = %d" % (1000, 200, 29))
print("%d / %d = %d" % (num1, num2, num1 / num2))
print("%f * %f = %f" % (num1, num2, num1 * num2))
print("%f * %f = %5.0f %10s" % (num1, num2, num1 * num2, "입니다"))
# %(데이터 형식) = 출력할 데이터 형식
# %d : 정수, %f : 실수 , %c : 한 글자, %s : 문자열

# 한 줄에 여러 개의 값을 출력하기
# end에 할당하는 값이 여러
print("test1")
print("test2")
print("test3")

print("test1", end=" ")
print("test2", end=" ")
print("test3")

