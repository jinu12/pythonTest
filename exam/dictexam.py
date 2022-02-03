# 1. 딕셔너리 만들기
dict1 = {"삼성전자": 82000, "LG전자": 152000}
for key, value in dict1.items():
    print("{} = {}".format(key, value))

# 2. 딕셔너리 만들고 참색하기
count = 0

dict2 = {
        "삼성전자": [81000, 82500, 90800, 89300, 90000],
        "LG전자": (150000, 149000,  151000, 144000, 152500)
        }
print(type(dict2["삼성전자"]))
print(type(dict2["LG전자"]))


for key, value in dict2.items():
    print("{} ".format(key), end="=> ")
    for data in value:
        count = count + 1
        print("가격{} : {}".format(count, data), end=" ")
    count = 0
    print("")

print(type(dict2["삼성전자"]))
print(type(dict2["LG전자"]))

#
# 3
soultion = False
dict3 = {
        "python": "pycharm",
        "web": "django",
        "arduino": "led",
        "raspberryPI": "carmera",
        "android": "android studio"
        }
while True:
    print("알고 싶은 과목은?", end="")
    for key, value in dict3.items():
        print("{}".format(key), end=",")
    print("")
    answer = input("")
    if answer == "q":
        break
    else:
        for key, value in dict3.items():
            if dict3[key] == dict3[answer]:
                # print("필요 장비 및 프로그램:{} -> {}".format(answer, dict3[answer]))
                soultion = True
        if soultion:
            print("필요 장비 및 프로그램:{} -> {}".format(answer, dict3[answer]))
        else:
            print("그런 과목은 없습니다. 다시 입력해주세요")

