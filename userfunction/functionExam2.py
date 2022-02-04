# functionExam1.py 파일에서 정의한 printgugu()와 printSum()을 copy해서 작업하기
# - printsum는 1~입력숫자 까지의 합 구하기
def printGugu(num=int(input("숫자를 입력해주세요 : "))):
    for i in range(1, 10):
        print("{} * {} = {}".format(num, i, num * i))


printGugu()

print("*" * 60)


def printSum(nums=int(input("숫자를 입력해주세요 : "))):
    total = 0
    for i in range(1, nums):
        total = total + i
    print("1부터 {}까지 합 => ".format(nums), total)


printSum()

print("*" * 60)
