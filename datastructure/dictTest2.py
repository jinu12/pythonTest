# 딕셔너리의 내장함수
dict1 = {1: "python", 2: "c", 3: "android", 4: "arduino"}
dict2 = {"key1": 10000, "key2": 20000, "key3": 40000, "key4": 50000}

print(dict1)
print("key=", dict1.keys())
# 딕셔너리에서 키만 추출
print("key=", list(dict1.keys()))

print("values=", dict1.values())
# 딕셔너리에 저장된 value만 추출
print("values=", list(dict1.values()))

print(dict1.items())

print(1 in dict1)
# 1이라는 키가 dict1이라는 딕셔너리에 존재하면 True를 리턴
print("1" in dict1)
print(type('1'))
print(type(1))
