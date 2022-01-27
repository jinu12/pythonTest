Sum = 0
odd = 0
even = 0
i = 1

while i < 101:
    Sum = Sum + i
    if i % 2 == 1:
        odd = odd + i
    else:
        even = even + i
    i = i + 1
print("총합 : %d" % Sum)
print("홀수합 : %d" % odd)
print("짝수합 : %d" % even)