# The Relation 

## 1. Relational Database

### 관계형 데이터베이스 
 - 데이터 간에 **관계**가 있는 데이터 항목들의 모음
 - 테이블, 행, 열의 정보를 구조화하는 방식
 - **서로 관련된 데이터 포인트를 저장**하고 이에 대한 **엑세스**를 제공

---

### 관계 
 - **여러 테이블 간의 (논리적) 연결**
 - 관계로 인해 할 수 있는 것
     - 이 관계로 인해 두 테이블을 사용하여 데이터를 다양한 형식으로 조회할 수 있음   
    (예를 들어, 특정 날짜에 구매한 모든 고객 조회, 지난달에 배송일이 지연된 고객 조히 등등)
--- 
### 관계형 데이터베이스 용어 

 ### 1) Table (aka Relation)
 - 데이터를 기록하는 곳 (데이터를 기록하는 최종 위치)
 - 모든 Table에는 행에서 고유하게 식별 가능한 기본 키라는 속성이 있으며, 외래 키를 사용하여 각 행에서 서로 다른 테이블 간의 관계를 만들 수 있음
 - 각 Table은 Database로 그룹핑됨

### 2) Field (aka Column, Attribute)
 - 각 필드에는 고유한 데이터 형식(타입)이 지정됨
 - 테이블에서의 열을 의미

### 3) Record (aka Row, Tuple)
 - 각 레코드에는 구체적인 데이터 값이 저장됨
 - 관계된 데이터의 묶음
 - 테이블에서의 행을 의미

### 4) Database (aka Schema)
 - 테이블의 집합(Set of tables)
 - 체계적인 데이터 모음으로, 데이터를 저장하고 조작
     - Create (저장)
     - Read (조회)
     - Update (갱신)
     - Delete (삭제)

### 5) Primary Key (PK)
 - 각 레코드의 고유한 값 (우리나라에서 사용하는 주민등록번호 같음)
 - 관계형 데이터베이스에서 **레코드의 식별자**로 활용

---

## 2. RDBMS (Relational Database Management System)
 - 관계형 데이터베이스를 관리하는 소프트웨어 프로그램
 - 데이터 저장 및 관리를 용이하게 하는 시스템
 - 데이터베이스와 사용자 간의 인터페이스 역할
     - 사용자가 데이터 구성, 업데이트, 모니터링, 백업, 복구 등을 할 수 있도록 도움

---     

### 대표적인 RDMBS
 - MySQL / PostgreSQL / Oracle Database / MS SQL Server / ....
 - **MYSQL**     
      - 가장 널리 사용되는 오픈소스 RDBMS
      - 다양한 운영체제에서 실행 가능
      - 여러 프로그래밍 언어를 위한 다양한 API 제공
      - MySQL Workbench Tool을 통해 그래픽 인터페이스를 제공(GUI)
      - 구조 : Table ⊂ Database ⊂ Database Server(MySQL)