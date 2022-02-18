# 1
SELECT t.titleno, e.empname, t.titlename, d.deptloc 
FROM emp e
INNER JOIN dept d
ON e.deptno = d.deptno
INNER JOIN title t
ON e.titleno = t.titleno
WHERE DATE_FORMAT(hdate,'%YYYY') > 2000;
# 2
SELECT d.deptname, AVG(e.salary) AS av
FROM emp e
INNER JOIN dept d
ON e.deptno = d.deptno
GROUP BY d.deptname
HAVING AVG(e.salary) >= 3000;
# 3
SELECT AVG(e.salary) AS av
FROM emp e
INNER JOIN dept d
ON e.deptno = d.deptno
WHERE d.deptloc = '대구';
# 4
SELECT (PERIOD_DIFF(DATE_FORMAT(NOW(),'%Y%m'), DATE_FORMAT(hdate,'%Y %m')))
FROM emp e
INNER JOIN dept d
ON e.deptno = d.deptno
WHERE e.empname = '홍영자';

SELECT TIMESTAMPDIFF(MONTH ,hdate, NOW()) AS 근속월수 FROM emp
WHERE deptno = (SELECT deptno FROM emp WHERE empname = '홍영자')
AND empname NOT IN ('홍영자');

# 5
SELECT ROW_NUMBER() OVER(ORDER BY e.salary DESC) AS rk, d.deptname, t.titlename, (YEAR(NOW()) - YEAR(e.hdate)) AS 연수 
FROM emp e
INNER JOIN dept d
ON e.deptno = d.deptno
INNER JOIN title t
ON e.titleno = t.titleno
GROUP BY e.hdate;



​

3. 경기 지역의 직원 들의 평균 연봉을 구하시오

​

4. 홍영자 직원와 같은 부서 직원들의 

근무 월수를 구하시오 

​SELECT  * FROM emp
 WHERE deptno = (SELECT deptno FRMO emp WHERE empname = '홍영자')
 AND empname NOT IN ('홍영자');

5. 입사 년수가 가장 많은 직원 순으로 

정렬 하여 순위를 정한다.

이름, 부서명, 직위, 년수