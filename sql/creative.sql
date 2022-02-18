DROP DATABASE IF EXISTS company2;
CREATE DATABASE company2;

USE company2;
DROP TABLE IF EXISTS emp,
           dept,
           title;

CREATE TABLE dept(
       deptno CHAR(2)
              PRIMARY KEY,
              deptname VARCHAR(20),
              deptloc  VARCHAR(20)
);

ALTER TABLE dept ADD CONSTRAINT dept_ch1 CHECK(
                        deptname IS NOT NULL
);

ALTER TABLE dept ADD CONSTRAINT dept_ch2 CHECK(
                        deptloc IS NOT NULL
);

CREATE TABLE title(
       titleno CHAR(2)
              PRIMARY KEY,
              titlename VARCHAR(20)
);

ALTER TABLE title ADD CONSTRAINT title_uq1 UNIQUE(
                        titlename
);

CREATE TABLE emp(
       empno INT AUTO_INCREMENT
              PRIMARY KEY,
              empname VARCHAR(30),
              deptno  CHAR(2),
              titleno CHAR(2),
              manager INT,
              salary  INT,
              hdate   DATE
);

ALTER TABLE emp AUTO_INCREMENT=100;

ALTER TABLE emp ADD CONSTRAINT fk1 FOREIGN KEY (
                        deptno
)
            REFERENCES dept(
                        deptno
);

ALTER TABLE emp ADD CONSTRAINT fk2 FOREIGN KEY (
                        titleno
)
            REFERENCES title(
                        titleno
);

ALTER TABLE emp ADD CONSTRAINT uq1 UNIQUE(
                        empname
);

ALTER TABLE emp ADD CONSTRAINT ch1 CHECK(
                        salary IS NOT NULL
);

ALTER TABLE emp ALTER COLUMN hdate SET DEFAULT CURDATE();