# 1부터 1000까지의 홀수의 합 짝수의 합, 총합을 출력하세요
Sum = 0
Odd = 0
Even = 0
Str = "1부터 1000까지"
for i in range(1, 1001, 1):
    Sum = Sum + i
    if i % 2 == 0:
        Even = Even + i
    else:
        Odd = Odd + i
print(Str + "의 총합 : {}".format(Sum))
print(Str + "홀수의 합 : {}".format(Odd))
print(Str + "짝수의 합 : {}".format(Even))

