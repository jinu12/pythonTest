# ws04.py
#
import math

total = 0
# 4. 10행 10열의 정방 행렬 구조의 지형이 있다

# 각 셀의 가로와 세로의 길이는 1미터라고 했을때  대각선의 길이를 구하시오.
for i in range(1, 11):
    total = total + i
width = total
vertical = total

diagonal = math.sqrt(vertical + width)

print("가로 : ", width)
print("세로 : ", vertical)
print("대각선 : ", diagonal)

