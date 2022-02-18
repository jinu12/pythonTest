#Join

# 1. INNER JOIN
SELECT e.empname, d.deptname, t.titlename 
FROM emp e
INNER JOIN dept d
ON e.deptno = d.deptno
INNER JOIN title t 
ON e.titleno = t.titleno;


SELECT e.empname, d.deptname, t.titlename, e.salary 
FROM emp e
INNER JOIN dept d
ON e.deptno = d.deptno
INNER JOIN title t 
ON e.titleno = t.titleno
WHERE e.salary > 3000
ORDER BY e.empname;

SELECT d.deptno, AVG(e.salary) AS av
FROM emp e
INNER JOIN dept d
ON e.deptno = d.deptno
GROUP BY d.deptno;

SELECT t.titlename, AVG(e.salary) AS av
FROM emp e
INNER JOIN title t 
ON e.titleno = t.titleno
GROUP BY t.titlename;

# 부서별 사우너과 대리의 연봉 평균을 구하시오.

SELECT d.deptname, AVG(e.salary) AS av
FROM emp e
INNER JOIN dept d
ON e.deptno = d.deptno
INNER JOIN title t
ON e.titleno = t.titleno
WHERE t.titlename IN ('대리','사원')
GROUP BY e.deptno
ORDER BY av DESC;

SELECT *
FROM emp e
INNER JOIN dept d
ON e.deptno = d.deptno
INNER JOIN title t
ON e.titleno = t.titleno;