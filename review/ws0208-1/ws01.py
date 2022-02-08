# ws01
print("ws01")
# 직원의 월급을 입력 받는다.
salary = int(input('월급을 입력해주세요 : '))
# 월 세금으로 3.8%를 공제하고
tax = salary * 0.038
# 세후 보험료는 10.2%를 공제 한다.
premium = salary * 0.102
# 이 직원의 연봉을 계산해서
afterSalaryYear = (salary - tax - premium) * 12
# 세금과보험료를 제외한 (월급과 연봉)을 출력 하고 세금과 보험료를 출력 한다.
print('월급 : {}, 연봉 : {} , 세금 : {} 보험료 : {}'.format(salary, salary * 12, tax, premium))

if afterSalaryYear <= 30000000:  # 연봉이 3000만원 이하면 '사원'
    print('사원')
elif afterSalaryYear <= 50000000:  # 연봉이 5000만원 이하면 '대리'
    print('대리')
elif afterSalaryYear <= 80000000:  # 연봉이 8000만원 이하면 '과장'
    print('과장')
else:
    print('정확한 월급을 입력해주세요.')