# #미니계산기
# 1.
Sum = 0
Dobble = 0
Minus = 0
Multiply = 0
Divide = 0
Str = "계산결과=>{}"
print("1.더하기\n2.곱하기\n3.빼기\n4.나누기\n연산자\n5.종료")

# 2.
while True:
    select = int(input("연산자를 선택하세요."))
    num = int(input("숫자를 입력하세요 "))
    print("", end="")
    num2 = int(input(""))
    if select == 1:
        Sum = num + num2
        print(Str.format(Multiply))
    elif select == 2:
        Multiply = num * num2
        print(Str.format(Multiply))
    elif select == 3:
        Minus = num - num2
        print(Str.format(Multiply))
    elif select == 4:
        Divide = num / num2
        print(Str.format(Multiply))
    elif select == 5:
        break
    else:
        print("잘못된 숫자를 입력하셨습니다.")

