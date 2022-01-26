# 1부터 100까지의 숫자의 총합 , 홀수합, 짝수합
Sum = 0
odd = 0
even = 0
for i in range(1, 101):
    Sum = Sum + i
    if i % 2 == 1:
        odd = odd + i
    else:
        even = even + i
print("총합 : %d" % Sum)
print("홀수합 : %d" % odd)
print("짝수합 : %d" % even)
