# SQL - Modifying Data

# 1. Insert data into table

## **INSERT** statement
 - 테이블 레코드 삽입

 - INSERT syntax
     - INSERT INTO 절 다음에 테이블 이름과 괄호 안에 필드 목록을 작성
     - VALUES 키워드 다음 괄호 안에 해당 필드에 삽입할 값 목록을 작성
```
INSERT INTO table_name (c1, c2, ...)
VALUES (v1, v2, ...);
```
```
 -- 예시
INSERT INTO 
    articles (title, content, createdAt)
VALUES 
	('title1', 'content1', '1900-01-01'),
    ('title2', 'content2', '1800-01-01'),
    ('title3', 'content3', CURDATE());

-- CURDATE() : "현재 날짜를 반환", MySQL이 제공하는 Date Functions 중 하나
```

--- 

# 2. Update data in table

## **UPDATE** statement
 - 테이블 레코드 수정

 - UPDATE syntax
     - SET 절 다음에 수정할 필드와 새 값을 지정
     - WHERE 절에서 수정할 레코드를 지정하는 조건 작성
         - WHERE 절을 작성하지 않으면 모든 레코드를 수정
```
UPDATE table_name
SET column_name = expression,
[WHERE
    condition];
```
```
-- 예시 1
UPDATE 
	articles
SET
	title = 'hahaha',
    content = 'hohoho'
WHERE
	id = 2;

```
```
-- 예시 2
-- articles 테이블 모든 레코드의 content 필드 값 중 문자열 'content'를 'TEST'로 변경
UPDATE
	articles
SET
	content = replace(content, 'content', 'TEST');

-- REPLACE : "지정된 문자열 변경", MySQL이 제공하는 String Functions 중 하나
```

---

# 3. Delete data from table

## DELETE statement
 - 테이블 레코드 삭제

 - DELETE syntax
     - DELETE FROM 절 다음에 테이블 이름 작성
     - WHERE 절에서 삭제할 레코드를 지정하는 조건 작성
         - WHERE 절을 작성하지 않으면 모든 레코드를 삭제
```
DELETE FROM table_name
[WHERE
    condition];
```
```
-- 예시
-- articles 테이블에서 가장 최근에 작성된 레코드 2개를 삭제

DELETE FROM
	articles
ORDER BY
	createdAt DESC
LIMIT 2;
```