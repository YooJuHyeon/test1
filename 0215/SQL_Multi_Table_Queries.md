# SQL - Multi Table Queries

# Joining tables

## JOIN clause
 - 둘 이상의 테이블에서 데이터를 검색하는 방법
 
## JOIN 종류
     - INNER JOIN
     - OUTER JOIN
         - LEFT JOIN
         - RIGHT JOIN

---

## INNER JOIN clause
 - 두 테이블에서 값이 일치하는 레코드에 대해서만 결과를 반환

### INNER JOIN syntax
```
SELECT
    select_list
FROM
    table1
INNER JOIN table2
    ON table1.fk = table2.pk;
```
 - FROM 절 이후 메인 테이블 지정(table1)
 - INNER JOIN 절 이후 메인 테이블과 조인할 테이블을 지정(table2)
 - ON 키워드 이후 조인 조건을 작성
     - 조인 조건은 table1과 table2 간의 레코드를 일치시키는 규칙을 지정

---

## LEFT JOIN clause
 - 오른쪽 테이블의 일치하는 레코드와 함께 왼쪽 테이블의 모든 레코드를 반환

### LEFT JOIN syntax
```
SELECT
    select_list
FROM
    table1
LEFT [OUTER] JOIN table2
    ON table1.fk = table2.pk;
```
 - FROM 절 이후 왼쪽 테이블 지정 (table1)
 - LEFT JOIN 절 이후 오른쪽 테이블 지정(table2)
 - ON 키워드 이후 조인 조건을 작성
     - 왼쪽 테이블의 각 레코드를 오른쪽 테이블의 모든 레코드와 일치시킴
 - OUTER 생략 가능

### LEFT JOIN 특징
 - 왼쪽은 무조건 표시하고, 매치되는 레코드가 없으면 NULL을 표시
 - 왼쪽 테이블 한 개의 레코드에 여러 개의 오른쪽 테이블 레코드가 일치할 경우, 해당 왼쪽 레코드를 여러번 표시

---

## RIGHT JOIN clause
 - 왼쪽 테이블의 일치하는 레코드와 함께 오른쪽 테이블의 모든 레코드 반환

### RIGHT JOIN syntax
```
SELECT
    select_list
FROM
    table1
RIGHT [OUTER] JOIN table2
    ON table1.fk = table2.pk;
```
 - FROM 절 이후 왼쪽 테이블 지정(table1)
 - RIGHT JOIN 절 이후 오른쪽 테이블 지정(table2)
 - ON 키워드 이후 조인 조건을 작성
     - 오른쪽 테이블의 각 레코드를 왼쪽 테이블의 모든 레코드와 일치시킴
 - OUTER은 생략 가능

### RIGHT JOIN 특징
 - 오른쪽은 무조건 표시하고, 매치되는 레코드가 없으면 NULL을 표시
 - 오른쪽 테이블 한 개의 레코드에 여러 개의 왼쪽 테이블 레코드가 일치할 경우, 해당 오른쪽 레코드를 여러 번 표시 

---

### 합집합
```
SELECT * FROM tableA
LEFT JOIN tableB ON tableA.fk = tableB.id
UNION
SELECT * FROM tableA
RIGHT JOIN tableB ON tableA.fk = tableB.id;
```
- UNION은 중복데이터 제거하여 출력
- UNION 대신 UNION ALL 쓰면 중복 여부와 상관 없이 모든 데이터 출력

---

### 차집합(A-B)
```
SELECT 
    *
FROM
    tableA
LEFT JOIN tableB
    ON tableA.fk = tableB.id
WHERE tableB.id IS NULL;
```