# 사용자지정의 함수를 만들기
def jobscheduler():
    print("*" * 30)
    print("작업시간:40")
    print("20시간을 보충하셔야 합니다.")
    print("*" * 30)
    print("")


# 2. 매개변수가 있고 리턴값이 없는 함수 정의

def jobscheduler2(name):
    print("*" * 30)
    print(name, "의 작업시간:40")
    print("20시간을 보충하셔야 합니다.")
    print("*" * 30)
    print("")


jobscheduler2("장동건")


# 3. 매개변수가 여러 개이고 리턴값이 없는 함수의 정의
#    매개변수가 여러 개인 경우 ,로 구분핟다.
def jobscheduler3(name, time):
    print("*" * 30)
    print(name, "의 작업시간:", time)
    print("20시간을 보충하셔야 합니다.")
    print("*" * 30)
    print("")


# 1. 매개변수가 없는 경우 호출
for i in range(3):
    jobscheduler()

# 2. 매개변수가 있고 리턴값이 없는 함수의 호출
jobscheduler2("장동건")
jobscheduler2("이유정")
jobscheduler2("아이유")

# 3. 매개변수가 여러 개 있고 리턴값이 업슨 함수의 호출
jobscheduler3("장동건", 20)
jobscheduler3("이유정", 40)
jobscheduler3("아이유", 50)

