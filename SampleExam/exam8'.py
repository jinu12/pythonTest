# 두 수의 최대 공약수를 구하는 프로그램을 작성하십시오.
avglists = []
avg = 0
print("입력값")

def gcd(*args):
    num1 = int(input(""))
    num2 = int(input(", "))
    if num1 < num2:
        for i in range(num1):
            if num1 % num2 == 0:
                avglists.append(i)
    return num1, num2

print(gcd())

# def gcd(num1, num2):
#     if num1 < num2:
#         for i in range(num1):
#             if num1 % num2 == 0:
#                 avglists.append(i)
#     return num1, num2