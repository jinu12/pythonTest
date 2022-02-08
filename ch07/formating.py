num1 = 10
num2 = 2.34
st = 'abc'

sql = 'INSERT INTO TB VALUES(%s,%d,%f)'
print(sql % (st, num1, num2))

sql2 = 'jwlee@tonesol.com'

id = sql2[0: sql2.find('@')]
print(id)

domain = sql2[sql2.find('@') + 1:]
print(domain)

# 3개의 숫자르 입력 받는다
# 3개의 숫자를 리스트에 담는다.
num = input('numbers : ')
nums = num.split()
print(nums)

lunums = []
for i in nums:
    lunums.append(int(i))
print(lunums)
