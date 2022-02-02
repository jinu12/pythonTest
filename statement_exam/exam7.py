# 총합 평균 구하기
total = 0
average = 0
count = 0

answerlist = [[5, 5, 5, 5, 5],
              [10, 10, 10, 10, 10],
              [20, 20, 20, 20, 20],
              [30, 30, 30, 30, 30]]
for i in range(0, 4):
    for j in range(0, 5):
        print(answerlist[i][j])
        total = total + answerlist[i][j]
        count = count + 1

print(total)
print(total/count)