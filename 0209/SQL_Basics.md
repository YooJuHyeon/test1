# SQL - Basics

## 1. SQL 

- Structure : 테이블의 형태로 **구조화**된 데이터 베이스
- Query : 에게 요청을 **질의(요청)**
- Language : 하는 프로그래밍언어
- SQL : 데이터베이스에 정보를 저장하고 처리하기 위한 프로그래밍 언어 (관계형 데이터베이스와의 대화)   

```
 SELECT column_name FROM table_name; 
```
 - SQL 키워드는 대소문자를 구분하지 않음
     - 하지만 대문자로 작성하는 것을 권장(명시적 구분)
 - 각 SQL Statements의 끝에는 세미콜론(;)이 필요
     - 세미콜론은 각 SQL Statements을 구분하는 방법   

---

## 2. SQL Statements

- SQL 언어를 구성하는 가장 기본적인 코드 블록

```
 SELECT column_name FROM table_name; 
```
- 해당 예시 코드는 SELECT Statement라 부름
- 이 Statement는 SELECT, FROM 2개의 keyword로 구성 됨

### SQL Statements 유형

 - 데이터베이스에서 수행 목적에 따라 대체로 4가지 범주로 나뉨
     - DDL - 데이터 정의
     - DQL - 데이터 검색
     - DML - 데이터 조작
     - DCL - 데이터 제어

|유형|역할|SQL 키워드|
|------|---|---|
|DDL (Data Definition Language)|데이터의 기본 구조 및 형식 변경|CREATE / DROP / ALTER|
|DQL (Data Query Language)|데이터 검색|SELECT|
|DML (Data Manipulation Language)|데이터 조작 (추가, 수정, 삭제)|INSERT / UPDATE / DELETE|
|DCL (Data Control Language)|데이터 및 작업에 대한 사용자 권한 제어|COMMIT / ROLLBACK / GRANT|

---
## Query
 - 질의, 질문
 - "데이터베이스로부터 정보를 요청"하는 것
 - 일반적으로 SQL로 작성하는 코드를 쿼리문(SQL문)이라 함

--- 
## 정리

- SQL은 데이터베이스와 상호작용하고, 데이터베이스에서 데이터를 반환하기 위한 언어
- 단순히 SQL 문법을 암기하고 상황에 따라 실행만 하는 것이 아닌
- SQL을 통해 관계형 데이터베이스를 잘 이해하고 다루는 방법을 학습

- SQL은 역할이 명확하게 정해져 있는 프로그래밍 언어(역할이 제한됨-데이터베이스에 CRUD)
