starlist = [10, 30, 20, 80,  50]
Sum = 0
for i in range(len(starlist)):
    Sum = Sum + starlist[i]
for i in range(len(starlist)):
    percent = starlist[i]/Sum * 100
    print("*"*int(percent),end="")
    print("({})".format(percent))