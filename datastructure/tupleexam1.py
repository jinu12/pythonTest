# 88, 99, 100점을 튜플로 정의하고 합계와 평균을 구해 출력하기
tuple1 = (88, 99, 100)
total = 0
for i in range(len(tuple1)):
    total = total + tuple1[i]
print("총합 : {}".format(total))
print("평균 : {}".format(total/len(tuple1)))
