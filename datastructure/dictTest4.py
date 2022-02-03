# 딕셔너리에 저장된 모든 요소를 추출하기
dict1 = {1: "python", 2: "c", 3: "python", 4: "arduino"}
dict2 = {"key1": 10000, "key2": 20000, "key3": 40000, "key4": 50000}
for key, value in dict1.items():
    print("{}={}".format(key, value))
print("=" * 30)

for key in dict1.keys():
    print("%d -> %s" % (key, dict1[key]))
print("*" * 30)

for key in dict1.keys():
    print("%d -> %s" % (key, dict1.get(key)))
print("*" * 30)

print("{:,} 입니다".format(dict2["key4"]))
