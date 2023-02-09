# SQL - Single Table Queries

# 1. Querying data

## SELECT 
- SELECT statement
- SELECT 문을 사용하여 테이블의 데이터를 **조회 및 반환**
- SELECT * (asterisk)를 사용하여 테이블의 모든 필드 선택

--- 

### SELECT syntax

```
SELECT
    select_list
FROM
    table_name;    
```
- SELECT 키워드 다음에 데이터를 선택하려는 필드를 하나 이상 지정
- FROM 키워드 다음에 데이터를 선택하려는 테이블의 이름을 지정

---

# 2. Sorting data

## ORDER BY
- ORDER BY clause
- 조회 결과의 레코드를 정렬

---

### ORDER BY syntax

```
SELECT
    select_list
FROM
    table_name
ORDER BY
    column1 [ASC¦DESC],
    column2 [ASC¦DESC],
    ...;   
```
 - FROM clause 뒤에 위치
 - 하나 이상의 컬럼을 기준으로 결과를 오름차순(ASC, 기본 값), 내림차순(DESC)으로 정렬할 수 있음

---

## SELECT statement 실행 순서

테이블에서(FROM) → 조회하여(SELECT) → 정렬(ORDER BY)
