CREATE TABLE `상품` (
	`Key`	int	NOT NULL,
	`Field2`	char(10)	NULL,
	`Field3`	int	NULL,
	`Field4`	int	NULL,
	`Field`	date	NULL,
	`Key2`	int	NOT NULL,
	`Key22`	char(10)	NOT NULL
);

CREATE TABLE `사용자` (
	`Key`	int	NOT NULL,
	`Key2`	char(10)	NOT NULL,
	`Field`	char(10)	NULL,
	`Field2`	varchar(30)	NULL,
	`Field3`	VARCHAR(255)	NULL,
	`Field4`	DATE	NULL
);

CREATE TABLE `주문` (
	`Key`	VARCHAR(255)	NOT NULL,
	`Key2`	int	NOT NULL,
	`Key22`	char(10)	NOT NULL,
	`Key3`	int	NOT NULL,
	`Field`	VARCHAR(255)	NULL
);

CREATE TABLE `판매자` (
	`Key`	int	NOT NULL,
	`Key2`	char(10)	NOT NULL,
	`Field2`	char(10)	NULL,
	`Field3`	char(10)	NULL,
	`Field4`	VARCHAR(255)	NULL
);

CREATE TABLE `판매 계시판` (
	`Key`	int	NOT NULL,
	`Key2`	int	NOT NULL,
	`Field`	char(10)	NULL,
	`Field2`	varchar(200)	NULL,
	`Field3`	date	NULL
);

CREATE TABLE `계시판 답글` (
	`Key2`	int	NOT NULL,
	`Key`	int	NOT NULL,
	`Field`	varchar(100)	NULL
);

CREATE TABLE `리뷰계시판` (
	`Key`	int	NOT NULL,
	`Field`	int	NULL,
	`Field2`	varchar(200)	NULL,
	`Field3`	date	NULL,
	`Key2`	int	NOT NULL,
	`Key22`	char(10)	NOT NULL
);

CREATE TABLE `리뷰답글` (
	`Key2`	int	NOT NULL,
	`Field`	varchar(100)	NULL,
	`Key`	int	NOT NULL
);

ALTER TABLE `상품` ADD CONSTRAINT `PK_상품` PRIMARY KEY (
	`Key`
);

ALTER TABLE `사용자` ADD CONSTRAINT `PK_사용자` PRIMARY KEY (
	`Key`,
	`Key2`
);

ALTER TABLE `주문` ADD CONSTRAINT `PK_주문` PRIMARY KEY (
	`Key`
);

ALTER TABLE `판매자` ADD CONSTRAINT `PK_판매자` PRIMARY KEY (
	`Key`,
	`Key2`
);

ALTER TABLE `판매 계시판` ADD CONSTRAINT `PK_판매 계시판` PRIMARY KEY (
	`Key`
);

ALTER TABLE `계시판 답글` ADD CONSTRAINT `PK_계시판 답글` PRIMARY KEY (
	`Key2`
);

ALTER TABLE `리뷰계시판` ADD CONSTRAINT `PK_리뷰계시판` PRIMARY KEY (
	`Key`
);

ALTER TABLE `리뷰답글` ADD CONSTRAINT `PK_리뷰답글` PRIMARY KEY (
	`Key2`
);

