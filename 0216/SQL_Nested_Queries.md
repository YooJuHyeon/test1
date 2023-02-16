# SQK - Nested Queries

# 1. Introduction to Subquery

## Subquery
 - "A query inside a query"
 - 단일 쿼리문에 여러 테이블의 데에터를 결합하는 방법

```SQL
-- Subquery 예시
-- table1 에서 가장 나이가 어린 사람을 삭제해야 한다면?

-- 1
SELECT MIN(age)
FROM table1;

-- 2
DELETE FROM table1
WHERE age = 위에서 찾은 최소값;


-- Subquery를 활용한 결과값 출력 (1+2)
DELETE FROM table1
WHERE age = (
    SELECT MIN(age) FROM table1
);
```

```SQL
-- Subquery 예시 (심화)
-- 소비를 한 고객들 중 한번에 지불한 금액이 가장 높은 고객의 customerNumber, amount, contactFirstName을 조회
-- 고객 테이블은 customers, 지불 테이블은 payments를 활용

-- 1
SELECT customerNumber, amount
FROM payment
WHERE amount = (
    SELECT MAX(amount)
    FROM payments
);

-- 2
SELECT contactFirstName,amount, payments.customerNumber
FROM payments
INNER JOIN customers
    ON payments.customerNumber = customers.customerNumber

-- 1 + 2
SELECT customerNumber, amount, contactFirstName
FROM (
    SELECT contactFirstName,amount, payments.customerNumber
    FROM payments
    INNER JOIN customers
     ON payments.customerNumber = customers.customerNumber
) AS findName
WHERE
    amount = (SELECT MAX(amount)) FROM payments);
```
 - 풀이과정
 1. payments 테이블과 customers 테이블을 조인하여 customerNumber, amount, contactFirstName 필드를 포함하는 findName이라는 이름의 서브쿼리를 생성
     - FROM 절에서 사용하는 subquery는 별도의 파생된 테이블로 간주되기 때문에 반드시 별칭 지정 필요
2. findName 서브쿼리에서 contactFirstName,amount, payments.customerNumber 필드를 선택
3. 또 다른 서브쿼리를 사용해서 payments 테이블에서 가장 높은 amount 값을 가진 레코드를 찾기
4. findName 서브쿼리에서 amount 필드와 다른 서브쿼리의 결과가 일치하는 레코드를 선택
5. 최종적으로 contactFirstName,amount, payments.customerNumber 필드를 출력

---

### Subquery 특징
 - 조건에 따라 하나 이상의 테이블에서 데이터를 검색하는 데 사용
 - SELECT, FROM, WHERE, HAVING 절 등에서 다양한 맥락에서 사용

---

## <span style="color:red"> EXISTS </span> operator
 - 쿼리 문에서 반환된 레코드의 존재 여부를 확인

### EXISTS syntax

```SQL
SELECT
    select_list
FROM
    table
WHERE
    [NOT] EXISTS (subquery);
```
- subquery가 하나 이상의 행을 반환하면 EXISTS 연산자는 true를 반환하고 그렇지 않으면 false를 반환
- 주로 WHERE 절에서 subquery의 반환 값 존재 여부를 확인하는데 사용

```SQL
-- EXISTS 예시
-- Paris에 있는 사무실에서 일하는 모든 직원의 번호, 이름, 성을 조회
-- 직원 테이블은 employees, 사무실 테이블은 offices이며, 두 테이블의 officeCode 필드를 기준으로 비교

SELECT
    employeenumber, firstname, lastname
FROM
    employees
WHERE
    EXISTS (
        SELECT *
        FROM offices
        WHERE city = 'Paris' AND offices.officeCode = employees.officeCode
    );
```

---

# 2. Conditional Statements

## <span style="color:red"> CASE </span> statement
 - SQL 문에서 조건문을 구성

### CASE syntax 

```SQL
CASE case_value
    WHEN when_value1 THEN statements
    WHEN when_value2 THEN statements
    ...
    [ELSE else-statements]
END CASE;
```
 - case_value가 when_value와 동일한 것을 찾을 때까지 순차적으로 비교
 - when_value와 동일한 case_value를 찾으면 해당 THEN 절의 코드를 실행
 - 동일한 값을 찾지 못하면 ELSE 절의 코드를 실행
     - ELSE 절이 없을 때 동일한 값을 찾지 못하면 오류 발생

```SQL
-- CASE 예시
-- orders 테이블의 status에 따라 상세 정보를 매겨 조회
-- 'In Process'는 '주문중', 'Shipped'는 '발주완료', 'Cancelled'는 '주문취소', 그 외는 '기타사유'로 지정
SELECT orderNumber, status,
    CASE
        WHEN status = 'In Process' THEN '주문중'
        WHEN status = 'Shipped' THEN '발주완료'
        WHEN status = 'Cancelled' THEN '주문취소'
        ELSE '기타사유'
    END AS details
FROM orders;
```