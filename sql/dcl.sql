SELECT salary , salary * 0.1 AS tax 
FROM emp;

SELECT * FROM emp 
WHERE salary < 4000 
AND DATE_FORMAT(hdate,'%YYYY') < 2001;

SELECT * 
FROM emp 
WHERE empname LIKE '%자%' IS NOT NULL;

SELECT empname, salary,
	CASE salary
	WHEN salary < 2000 THEN '하' 
	WHEN salary < 4000 THEN '중'
	ELSE '고'  
	END AS grade
FROM emp;

# NULL CHECK
SELECT empno, IFNULL(manager, '없음') FROM emp;

# 이영자가 속한 부서의 평균 보다 많이 받는 직원을 조회

# CONCAT

SELECT CONCAT(titleno, '+', deptno, '+', empname, salary) FROM emp;

# 순 위

SELECT ROW_NUMBER() OVER(ORDER BY salary DESC) AS rk , empname, salary FROM emp LIMIT 3;

SELECT DENSE_RANK() OVER(ORDER BY salary DESC) AS rk , empname, salary FROM emp;

# json

SELECT JSON_OBJECT('name', empname, 'sal', salary) FROM emp;

