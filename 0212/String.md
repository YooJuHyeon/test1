# 문자열(String)
 - 문자열은 immutable(변경 불가능한) 자료형!

## 1. 문자열 조작

### 문자열 슬라이싱
 - s = 'abcdefghi'   

| |a|b|c|d|e|f|g|h|i|
|------|---|---|------|---|---|------|---|---|--|
|index|0|1|2|3|4|5|6|7|8|
|index|-9|-8|-7|-6|-5|-4|-3|-2|-1|

```
 s[2:5] = 'cde'
 s[-6:-2] = 'defg'
 s[2:5:2] = 'ce'
 s[-6:-1:3] = 'dg'
 s[2:5:-1] = ''
 s[:3] = 'abc'
 s[5:] = 'fghi'
 s[:] = 'abcdefghi' 
 s[::-1] = 'ihgfedcba'
```
---

## 2. 문자열 메서드

### 1) .split(기준 문자)
 - 문자열을 일정 **기준**으로 나누어 **리스트로 반환**
 - 괄호 안에 아무것도 넣지 않으면 자동으로 공백을 기준으로 설정
```
word1 = "I play the piano"
print(word1.split())
# ['I', 'play', 'the', 'piano']

word2 = "apple,banana,orange,grape"
print(word2.split(","))
# ['apple', 'banana', 'orange', 'grape']

word3 = "This_is_snake_case"
print(word3.split("_"))
# ['This', 'is', 'snake', 'case']
```

### 2) .strip(제거할 문자)
 - 문자열의 **양쪽** 끝에 있는 특정 문자를 모두 **제거**한 새로운 문자열 반환
 - 괄호 안에 아무것도 넣지 않으면 자동으로 공백을 제거 문자로 설정
 - 제거할 문자를 여러 개 넣으면 해당하는 모든 문자들을 제거
 ```
word1 = " Hello World "
print(word1.strip())
# Hello World

word2 = "aHello Worlda"
print(word2.strip("a"))
# Hello World

word3 = "Hello World"
print(word3.strip("Hd"))
# ello Worl

word4 = "Hello Worldddddd"
print(word4.strip("d"))
# Hello Worl
 ```

### 3) .find(찾는 문자)
 - 특정 문자가 처음으로 나타나는 **위치(index)**를 반환
 - 찾는 문자가 없다면 **-1**을 반환
 ```
word1 = "apple"
print(word1.find("p"))
# 1

word2 = "apple"
print(word2.find("k"))
# -1
 ```

### 4) .index(찾는 문자)
 - 특정 문자가 처음으로 나타나는 **위치(index)**를 반환
 - 찾는 문자가 없다면 **오류** 발생 
 ```
word1 = "apple"
print(word1.index("p"))
# 1

word2 = "apple"
print(word2.index("k"))
# ValueError: substring not found
 ```

### 5) .count(개수를 셀 문자)
 - 문자열에서 특정 문자가 **몇 개**인지 반환
 - 문자 뿐만 아니라, 문자열의 개수도 확인 가능

```
word1 = "banana"
print(word1.count("a"))
# 3

word2 = "banana"
print(word2.count("ana"))
# 1
```

### 6) .replace(기존 문자, 새로운 문자)
 - 문자열에서 기존 문자를 새로운 문자로 **수정한** 새로운 문자열 반환
 - 특정 문자를 빈 문자열("")로 수정하여 마치 해당 문자를 삭제한 것 같은 효과 가능
 ```
 word1 = "happyhacking"
print(word1.replace("happy", "angry"))
# angryhacking

word2 = "happyhacking"
print(word2.replace("h", "H"))
# HappyHacking

word3 = "happyhacking"
print(word3.replace("happy", ""))
# hacking
 ```

### 7) 삽입할 문자.join(iterable)
- iterable의 **각각 원소 사이에 특정 문자를 삽입한** 새로운 문자열 반환
- 공백 출력, 콤마 출력 등 **원하는 출력** 형태를 위해 사용
```
word1 = "happyhacking"
print(" ".join(word1))
# h a p p y h a c k i n g

word2 = "happyhacking"
print(",".join(word2))
# h,a,p,p,y,h,a,c,k,i,n,g

word3 = ["edu", "hphk.kr"]
print("@".join(word3))
# edu@hphk.kr

word4 = ["h", "a", "p", "p", "y"]
print("".join(word4))
# happy
```
---
- 문자열 탐색/검증

|문법|설명|
|:---|:---|
|s.find(x)|x의 첫 번째 위치를 반환. 없으면, -1을 반환|
|s.index(x)|x의 첫 번째 위치를 반환. 없으면, 오류 발생|
|s.isalpha()|알파벳 문자 여부. 단순 알파벳이 아닌 유니코드 상 Letter(한국어도 포함)|
|s.isupper()|대문자 여부|
|s.islower()|소문자 여부|
|s.istitle()|타이틀 형식 여부|

- 문자열 변경

|문법|설명|
|:---|:---|
|s.replace(old, new[,count ])|바꿀 대상 글자를 새로운 글자로 바꿔서 반환|
|s.strip([chars ])|공백이나 특정 문자를 제거|
|s.split(sep=None, maxsplit=-1)|공백이나 특정 문자를 기준으로 분리|
|'separator'.join([iterable ])|구분자로 iterable을 합침|

--- 

## 3. 아스키(ASCII) 코드

- 컴퓨터로 저장되고 처리되는 모든 데이터들은 2진수 형태로 정수화 되어야 하는데,
- 컴퓨터에 문자를 저장하는 방법으로 아스키코드(ASCII Code)나 유니코드(Unicode)가 자주 사용된다.
- 예를 들어, 영문 대문자 'A'는 10진수 값 65 로 표현하고, 
- 2진수(binary digit) 값 1000001 로 바꾸어 컴퓨터 내부에 저장한다. 
- 유니코드(unicode)는 세계 여러 나라의 문자를 공통된 코드 값으로 저장할 때 사용하는 표준 코드이다.

### 1) ord(문자)
- **문자 → 아스키코드** 로 변환하는 내장함수

### 2) chr(아스키코드)
- **아스키코드 → 문자** 로 변환하는 내장함수