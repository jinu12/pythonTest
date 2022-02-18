#1. emp 정보를 조회 한다. 
#emp 직원들의 모든 정보와 사원의 Manager 정보 까지 조회 한다.
#출력 정보 
#empno, empname, titlename, mgrname

#2. emp 정보를 조회 한다. 
#모든 emp 직원들의 모든 정보와 사원의 Manager명 정보 까지 조회 한다.
#추가 적으로 의 부서명,타이틀명 까지 출력 한다.

SELECT e.empno, e.empname, t.titlename, m.empname FROM emp e
INNER JOIN title t 
ON e.titleno = t.titleno
LEFT JOIN emp m 
ON e.manager = m.empno 
WHERE t.titlename = '사원';

#e.*, m.empname,d.deptname, t.titlename
#2
SELECT *
FROM emp e
INNER JOIN dept d
ON d.deptno = e.deptno
INNER JOIN title t 
ON t.titleno = e.titleno
LEFT JOIN emp m 
ON e.manager = m.empno 
ORDER BY e.salary DESC;companycompany