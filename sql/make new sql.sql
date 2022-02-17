SELECT * FROM emp;

SELECT *
FROM emp
WHERE salary > (SELECT AVG(salary/12) FROM emp WHERE empname ='이영자');
# 이름이 '홍정국'보다 큰 직원의 이름과 총수을 cnt로  출력하시요.


SELECT * FROM emp;

SELECT empname , COUNT(empname) AS cnt
FROM emp
WHERE salary > (SELECT salary FROM emp WHERE empname ='홍정국');


# 8 deptno : 10 -> SEOUL
SELECT * FROM emp
WHERE deptno = (
SELECT deptno FROM dept WHERE deptloc = '서울'
);

# Q. 부산에서 근무하는 2000년 이후 입사한 직원의 연봉평균과 대전에서 근무하는 
# 2000년 이후 입사한 직원의 연봉평균을 부서번호와 함께 출력하세요.

SELECT deptno, AVG(salary), empname 
FROM emp
WHERE deptno IN (SELECT deptno FROM dept WHERE deptloc IN ('서울','부산') AND YEAR(hdate) >= 2000  )
AND YEAR(hdate) >= 2000
GROUP BY deptno;

SELECT deptno, AVG(salary), empname 
FROM emp
WHERE deptno IN (20,40) AND YEAR(hdate) >= 2000
GROUP BY deptno;

SELECT deptno, AVG(salary) FROM emp
WHERE deptno IN (SELECT deptno from dept WHERE deptloc = '부산' OR deptloc = '대전') 
AND YEAR(hdate) >= 2000
GROUP BY deptno;

SELECT empname, salary,
CASE salary
WHEN salary < 2000 THEN '하'
WHEN salary < 4000 THEN '중'
ELSE '고'
END AS grade
FROM emp;

#연봉 순위를 rk로 출력하고 연봉순위가 5등이상인 살망의 이름과 부서번호, 랭킹를 출력하시오.
SELECT ROW_NUMBER() OVER(ORDER BY salary DESC) AS rk
FROM emp;

SELECT ROW_NUMBER() OVER(ORDER BY salary DESC) AS rk, empname
FROM emp
WHERE rk > 5;



# 이름이 '홍정국'보다 연봉이 큰 직원의 이름과 총수을 cnt로  출력하시요.


SELECT * FROM emp;

SELECT empname , COUNT(empname) AS cnt
FROM emp
WHERE salary > (SELECT salary FROM emp WHERE empname ='홍정국');




#Q.  30번 부서의 최고 연봉보다 높은 사원의 이름, 급여를 출력하세요.

SELECT *FROM emp;

WHERE deptno='30'

SELECT MAX(salary) FROM emp WHERE deptno='30';

SELECT empname, salary
FROM emp
WHERE sal > (SELECT MAX(salary)
FROM emp
WHERE deptno='30');
