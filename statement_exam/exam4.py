# 주어진 리스트이 최소갑 최빈값 구하기
answerlist = [79, 88, 91, 33, 100, 55, 95]
answermaxlist = []
answerlastlist = []
count = 0
answermax = 0
for i in range(len(answerlist)):
    for j in range(len(answerlist)):
        if answerlist[i] < answerlist[j]:
            count = count + 1
            answermaxlist.append(answerlist[j])
for i in range(len(answerlist)):
    for j in range(len(answerlist)):
        if answerlist[i] > answerlist[j]:
            answerlastlist.append(answerlist[j])
print("최빈값 : {}".format(answermaxlist[count-1]))
print("최빈값 : {}".format(answerlastlist[count-1]))


