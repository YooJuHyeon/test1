# SQL - Advanced 01

# 1. Transactions

## Transaction
 - (다 성공하던지 혹은 다 실패하던지 해야하는) 여러 쿼리문을 묶어서 하나의 작업처럼 처리하는 방법
 - 쪼개질 수 없는 업무처리의 단위
 - 전체가 수행되거나 또는 전혀 수행되지 않아야 함(All or Nothing)
---

### Transaction Syntax

```SQL
START TRANSACTION;
state_ments;
...
[ROLLBACK¦COMMIT];
```
 - START TRANSACTION
     - 트랜잭션 구문의 시작을 알림
 - COMMIT
     - 모든 작업이 정상적으로 완료되면 한꺼번에 DB에 반영
 - ROLLBACK
     - 부분적으로 작업이 실패하면 트랜잭션에서 진행한 모든 연산을 취소하고 트랜잭션 실행 전으로 되돌림

---

# 2. Triggers

## Triggers
 - 특정 이벤트(INSERT, UPDATE, DELETE)에 대한 응답으로 자동으로 실행되는 것

---

### Triggers Syntax
```SQL
CREATE TRIGGER trigger_name
    {BEFORE ¦ AFTER} {INSERT ¦ UPDATE ¦ DELETE}
    ON table_name FOR EACH ROW
    trigger_body;
```
 - CREATE TRIGGER 키워드 다음에 생성하려는 트리거의 이름을 지정
 - 각 레코드의 어느 시점에 트리거가 실행될지 지정(삽입, 수정, 삭제 전/후)
 - ON 키워드 뒤에 트리거가 속한 테이블의 이름을 지정
 - 트리거가 활성화될 떄 실행할 코드를 trigger_body에 지정
     - 여러 명령문을 실행하려면 BEGIN END 키워드로 묶어서 사용
 - **트리거는 DML의 영향을 받는 필드 값에만 적용할 수 있음**

 ---
## 참고

### Triggers 관련 추가 명령문
 ```SQL
 -- 트리거 목록 확인
 SHOW TRIGGERS;

 -- 트리거 삭제
 DROP TRIGGER trigger_name;
 ```

### Triggers 생성 시 에러 해결

- 트랜잭션 생성 후 정상적으로 종료되지 않아 발생하는 에러 발생 시 해결법
- Error Code:2013.Lost connection to MySQL server during query
- Error Code:2015.Lock wait timeout exceeded; try restarting transaction

```SQL
-- 실행중인 프로세스 목록 확인
SELECT * FROM information_schema.INNODB_TRX;

-- 특정 프로세스의 trx_mysql_thread_id 삭제
KILL [trx_mysql_thread_id1];
```