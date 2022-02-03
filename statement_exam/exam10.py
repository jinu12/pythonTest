# 구구단
gulist = []
danlist = []
for i in range(2, 10):
    for j in range(1, 10):
        gulist.append("{} * {} = {}".format(i, j, i*j))
for i in range(len(gulist)):
    print(gulist[i])

