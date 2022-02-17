
김진우

SELECT salary , salary * 0.1 AS tax FROM emp;

SELECT * FROM emp WHERE salary < 4000 AND DATE_FORMAT(hdate,'%YYYY') < 2001;

SELECT * FROM emp WHERE empname LIKE '%자%';

SELECT empname, salary,
CASE salary
WHEN salary < 2000 THEN '하'
WHEN salary < 4000 THEN '중'
ELSE '고'
END AS grade
FROM emp;

#5. 부서 별 월급의 평균을 구하시오
#단, 평균이 3000 이상인 부서만 출력

SELECT AVG(salary)
FROM emp
WHERE salary >= 3000
ORDER BY deptno;


#6. 부서 별 대리와 사원 연봉의 평균을 구하시오
#단, 평균이 2500 이상인 부서만 출력
SELECT deptno, AVG(salary) as salaryavg
FROM emp
WHERE titleno IN (10, 20)
GROUP BY deptno
HAVING AVG(salary) >= 2500;

# 7. 2000년 부터 2002년에 입사는 직원들의
# 월급의 평균을 구하시오
SELECT AVG(salary) AS av FROM emp
WHERE DATE_FORMAT(hdate, '%YYYY') BETWEEN 2000 AND 2002;

#8. 서울에서 근무하는 직원들을 조회 하시오
SELECT *
FROM emp
WHERE deptno = (SELECT deptno FROM dept WHERE deptloc = '서울');

#9. 이영자가 속한 부서의 직원 월급평균 보다 많이 받는 직원들을 조회 하시오

SELECT *
FROM emp
WHERE salary > (SELECT AVG(salary/12) FROM emp WHERE empname ='이영자');


#10. 김강국의 타이틀과 같은 직원들의 연봉보다 많이 받는 직원 들 중 2000 이전 입사한 직원들을 조회 하시오

SELECT *
FROM emp
WHERE salary > (SELECT salary FROM emp WHERE empname ='김강국')
AND DATE_FORMAT(hdate, '%YYYY') < 2000;