# 딕셔너리 생성
dict1 = {1: "python", 2: "python", 3: "arduino"}
print(dict1)
print(type(dict1))

dict2 = {"key1": 10000, "key2": 200000, "key3": 30000, "key4": 40000}
print(dict2)
print(type(dict2))

# 딕셔너리의 각 요소 엑세스
print(dict1[1])
print(dict2["key2"])

subject = dict1[1]
price = dict2["key1"]
# price = dict2.get("key2")
print("{} = {}".format(subject, price))

subject = dict1[1]
price = dict2.get("key2")
print("{} = {}".format(subject, price))

subject = dict1.get(7)
# 키가 없는 경우 에러를 발생시키지 않고
# price = dict2["key7"]
# 키가 없는 경우 에러를 발생
print("{} = {}".format(subject, price))
