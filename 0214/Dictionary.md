# 딕셔너리 (Dictionary)

## 1. 해시 테이블

- 파이썬에는 딕셔너리(dict) 자료구조가 내장되어 있다.
- 해시 함수 : 임의 길이의 데이터를 고정 길이의 데이터로 매핑하는 함수
- 해시 : 해시 함수를 통해 얻어진 값
```
{
    "name": "kyle",
    "gender": "male",
    "address": "Seoul"
}
 
 - Non-sequence & Key-Value
 - Non-sequenced은 비순차 자료형으로, 순서 개념이 없고, 인덱스를 이용한 접근 불가
 - Key는 immutable(변경 불가능) 
```
---

### 파이썬 딕셔너리의 특징
 - 해시 함수와 해시 테이블을 이용하기 때문에, 삽입, 삭제, 수정, 조회 **연산의 속도가 리스트보다 빠르다.** (해시 함수를 이용한 산술 계산으로 값이 있는 위치를 바로 알 수 있기 때문에)

---

### 딕셔너리는 언제 사용 해야할까?
 1. Key, Value 구조로 관리를 해야 하는 경우(순서나 인덱스가 아닌 경우)
 2. 데이터에 대한 빠른 접근 탐색이 필요한 경우

---

### 파이썬 리스트와 딕셔너리 비교

|연산 종류|딕셔너리|리스트|
|-------------|-----------|-------|
|Get Item|O(1)|O(1)|
|Insert Item|O(1)|O(1) 또는 O(N)|
|Update Item|O(1)|O(1)|
|Delete Item|O(1)|O(1) 또는 O(N)|
|Search Item|O(1)|O(N)|

---

## 2. 딕셔너리 기본 문법

### 기본적인 딕셔너리 사용법

 - **선언**
     - 변수 = {key1:value1, key2:value2,...}
```
a = {
    "name": "kyle",
    "gender": "male",
    "address": "Seoul"
}

print(a)

# {'name': 'kyle', 'gender': 'male', 'address': 'Seoul'}
```

 - **삽입/수정**
     - 딕셔너리[key] = value
     - 내부에 해당 key가 없으면 삽입, 있으면 수정

```
# 삽입

a = {
    "name": "kyle",
    "gender": "male",
    "address": "Seoul"
}
a["job"] = "coach"

print(a)

# {'name': 'kyle', 'gender': 'male', 'address': 'Seoul', 'job': 'coach'}
```

```
# 수정

a = {
    "name": "kyle",
    "gender": "male",
    "address": "Seoul"
}
a["name"] = "justin"

print(a)

# {'name': 'justin', 'gender': 'male', 'address': 'Seoul'}
```

 - **삭제**
     - 딕셔너리.pop(key)
     - 내부에 존재하는 key에 대한 value 삭제 및 반환, 존재하지 않는 key에 대해서는 KeyError 발생

```
a = {
    "name": "kyle",
    "gender": "male",
    "address": "Seoul"
}
gender = a.pop("gender")

print(a)
print(gender)

# {'name': 'kyle', 'address': 'Seoul'}
# male

```

 - **삭제**
     - 딕셔너리.pop(key,default)
     - 두 번째 인자로 default(기본)값을 지정하여 KeyError 방지 가능

```
a = {
    "name": "kyle",
    "gender": "male",
    "address": "Seoul"
}
phone = a.pop("phone", "010-1234-5678")

print(a)
print(phone)

# {'name': 'kyle', 'gender': 'male', 'address': 'Seoul'}
# 010-1234-5678

```

 - **조회**
     - Key에 해당하는 value 반환
     - 딕셔너리[key]
     - 딕셔너리.get(key)
     - 딕셔너리.get(key,default)

```
a = {
    "name": "kyle",
    "gender": "male",
    "address": "Seoul"
}

print(a["name"])            # kyle
print(a.get("name"))        # kyle
print(a["phone"])           # KeyError: 'phone'
print(a.get("phone"))       # None
print(a.get("phone","없음")) # 없음
```

---

### 딕셔너리 기본 문법 정리

 - 선언  :  변수 = {key1:value1, key2:value2,...}
 - 삽입/수정  :  딕셔너리[key] = value
 - 삭제  :  딕셔너리.pop(key,default)
 - 조회  :  딕셔너리[key] / 딕셔너리.get(key,default)

---

## 3. 딕셔너리 메서드

### .keys()
 - 딕셔너리 **key 목록**이 담긴 dict_keys 객체 반환

```
a = {
    "name": "kyle",
    "gender": "male",
    "address": "Seoul"
}

print(a.keys())     
# dict_keys(['name', 'gender', 'address'])

for key in a.keys():    
    print(key)
# name
# gender
# address

for key in a:
    print(key)
# name
# gender
# address
```

### .values()
 - 딕셔너리의 **value 목록**이 담긴 dict_values 객체 반환

```
a = {
    "name": "kyle",
    "gender": "male",
    "address": "Seoul"
}

print(a.values())     
# dict_values(['kyle', 'male', 'Seoul'])

for value in a.values():    
    print(value)
# kyle
# male
# Seoul
``` 

## .items()
 - 딕셔너리의 **(key, value) 쌍 목록**이 담긴 dict_items 객체 반환

```
a = {
    "name": "kyle",
    "gender": "male",
    "address": "Seoul"
}

print(a.items())     
# dict_items([('name', 'kyle'), ('gender', 'male'), ('address', 'Seoul')])

for item in a.items():    
    print(item)
# ('name', 'kyle')
# ('gender', 'male')
# ('address', 'Seoul')

for key, value in a.items():
    print(key, value)
# name kyle
# gender male
# address Seoul
```

---
## 참고
### Counter
 - 해시 가능한 객체를 세는 데 사용하는 딕셔너리 서브 클래스
 ```
 from collections import Counter

  # 반복 가능한 걸 넣으면 딕셔너리 형태로 만들어줌
 ```
 - [counter/파이썬 문서](https://docs.python.org/ko/3/library/collections.html#collections.Counter)
 
--- 

### 활용 연습 문제
 
 - [1](http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=4372&sca=pyd0)
 - [2](http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=4373&sca=pyd0)
 - [3](http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=4380&sca=pyd0)
