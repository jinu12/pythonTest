# range를 이용해서 for문을 처리

mydata = list(range(1, 10, 2))
print(mydata)

for i in range(1, 7):
    if i % 2 == 1:
        print("%d : 지금은 python 기본 학습중" % i)
    else:
        print("%d : 꽝 " % i)

print('##################################')

for i in range(1, 10, 2):
    print('지금은 python 기본 학습중!!')

print('##################################')

for i in range(10):
    print('지금도 학습중!!')

print('##################################')

# 1부터 10까지의 항목 출력하기
mynum = 0
hap = 0
for mynum in range(1, 11, 1):
    hap = hap + mynum
    print("현재 mynum은 : %d" % hap)
    print("현재 hap은 : %d" % mynum)
print(hap)

