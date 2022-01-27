# 88, 99, 77. 100, 99의 점수를 저장할 수 있는 리스트를 작성한 후 점수의 총합과 평균을 계산해서 출력하세요
# [출력 형태]
# 점수 총합 :
# 평균 :
List = [88, 99, 77, 100, 99]
Sum = 0

for i in List:
    Sum = Sum + i
avg = Sum / len(List)
print("점수 총합 : ", Sum)
print("평균 : ", avg)
