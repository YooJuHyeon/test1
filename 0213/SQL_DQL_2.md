# SQL - Single Table Queries

# 3. Filtering data
 - 데이터를 필터링하여 중복 제거, 조건 설정 등  SQL Query를 제어하기

## Filtering data 관련 Keywords
 - Clause
     - DISTINCT
     - WHERE
     - LIMIT
 - Operator
     - BETWEEN
     - IN
     - LIKE
     - Comparison
     - Logical

---
## **DISTINCT** clause
 - 조회 결과에서 중복된 레코드를 제거   

```
-- DISTINCT syntax

SELECT DISTINCT
    select_list
FROM
    table_name;
```

 - SELECT 키워드 바로 뒤에 작성해야 함
 - SELECT DISTINCT 키워드 다음에 고유한 값을 선택하려는 하나 이상의 필드를 지정

 ---

## **WHERE** clause
 - 조회 시 특정 검색 조건을 지정
 - FROM clause 뒤에 위치
 - search_condition은 **비교연산자** 및 **논리연산자**(AND, OR, NOT 등)를 사용하는 구문이 사용됨

```
-- WHERE syntax 

SELECT
    select_list
FROM
    table_name
WHERE
    search_condition;
```

---

## Comparison Operators (비교 연산자)
- ###  =, >=, <=, !=, IS, LIKE, IN, BETWEEN...AND
## Logical Operators (논리 연산자)
- ### AND(&&), OR(¦¦), NOT(!)

---

### 1) BETWEEN A AND B : 조건 A에서 조건 B 사이의 값을 조회
```
-- 예시1
WHERE
    officeCode BETWEEN 1 AND 4;

-- 예시2
WHERE
    officeCode >= 1
    AND officeCode <= 4;

-- 예시 1과 예시 2는 동일한코드 (officeCode 필드 값이 1에서 4 사이 값)
```

### 2) **IN** operators
- 값이 특정 목록 안에 있는지 확인
- IN (값1, 값2, 값3 ...) : 값이 값1 또는 값2에 해당하는 값만 출력)
- NOT IN (값1, 값2, 값3 ...) : 값이 값1, 값2, 값3 어디에도 해당하지 않는 것만 출력
```
-- 예시3
WHERE
    officeCode IN (1, 3, 4);

--예시4
WHERE
    officeCode = 1
    OR officeCode = 3
    OR officeCode = 4;   

-- 예시 3과 예시 4는 동일한코드 (officeCode 필드 값이 1또는 3또는 4값)    
```

### 3) **LIKE** operator
 - 값이 특정 패턴에 일치하는지 확인 with Wildcards
 - '%' : **0개 이상의 문자열**과 일치하는지 확인
 - '_' : **단일 문자**와 일치하는지 확인

 - 몇 가지 예시    
    |LIKE Operator|Description|
    |-------------|-----------|
    |WHERE CustomerName LIKE 'a%'|"a"로 시작하는 모든 값|
    |WHERE CustomerName LIKE '%a'|"a"로 끝나는 모든 값|
    |WHERE CustomerName LIKE '%or%'|"or"이 있는 모든 값|
    |WHERE CustomerName LIKE '_r%'|두 번째 인덱스에 "r"이 있는 모든 값|
    |WHERE CustomerName LIKE 'a_%_%'|"a"로 시작하며 최소 3글자 이상인 모든 값|
    |WHERE CustomerName LIKE 'a%o'|"a"로 시작하여 "o"로 끝나는 모든 값|

```
-- 예시5 (firstName 필드 값이 4자리면서 y로 끝나는 데이터)

WHERE
    firstName LIKE '___y';
```
---

## **LIMIT** clause
 - 조회하는 레코드 수를 제한
 - LIMIT clause는 하나 또는 두 개의 인자를 사용(0 또는 양의 정수)
 - row_count는 조회할 최대 레코드 수를 지정

```
-- LIMIT syntax

SELECT
    select_list
FROM
    table_name
LIMIT [offset,] row_count;
``` 

---

# 4. Grouping data

## **GROUP BY** clause
 - 레코드를 그룹화하여 요약본 생성 with 집계 함수

## Aggregation Functions
 - 값에 대한 계산을 수행하고 단일한 값을 반환하는 함수
 - SUM, AVG, MAX, MIN, COUNT

```
-- GROUP BY syntax

SELECT
    c1, c2, ..., cn, aggregation functions(ci)
FROM
    table_name
GROUP BY
    c1, c2, ..., cn;
```
 - FROM 및 WHERE 절 뒤에 배치
 - GROUP BY 절 뒤에 그룹화할 필드 목록을 작성

---
### **HAVING** clause
 - 집계 항목에 대한 세부 조건을 지정
     - 주로 GROUP BY와 함께 사용되며 GROUP BY가 없다면 WHERE처럼 동작
```
-- 예시
-- 테이블 customers에서 country필드를 그룹화하여 각 그룹에 대한 creditLimit의 평균 값이 80000을 초과하는 데이터만 조회

SELECT
    country,
    AVG(creditLimit)
FROM
    customers
GROUP BY
    country
HAVING
    AVG(creditLimit) > 80000;
```

---

# SELECT statement 실행 순서
 1. 테이블에서 (**FROM**)
 2. 특정 조건에 맞춰(**WHERE**) 
 3. 그룹화 하고(**GROUP BY**)
 4. 만약 그룹 중에서 조건이 있다면 맞추고(**HAVING**)
 5. 조회하여(**SELECT**)
 6. 정렬하고(**ORDER BY**)
 7. 특정 위치의 값을 가져온다(**LIMIT**)

---

## 참고
## 정렬에서의 NULL
 - MySQL에서 NULL은 NULL이 아닌 값 앞에 위치
     - NULL 값이 존재할 경우 오름차순 정렬 시 결과에 NULL이 먼저 출력
     