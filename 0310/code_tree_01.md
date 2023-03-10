# 기본 출력
## 1. 문자열에 특수 문자 포함시키기

### 방법 1) ' 문자 또는 " 문자로 감싸주기 (반대되는 문자 활용)
```python
print("Let's do it")
# Let's do it
```
### 방법 2) 특수문자 앞에 \ 붙이기
 - "와 '를 동시에 사용해야 하는 경우라면 해당 문자 앞에 \를 붙여주기
 ```python
 print('Let\'s do it')
 # Let's do it
 ```
### 방법 3) """ 혹은 '''로 전체 문장을 감싸기
```python
print('''Let's do it''')
# Let's do it
```

## 2. 줄바꿈 출력하기
### 방법 1) print 여러번 사용
```python
print("Hello World")
print("Python is Fun")

# Hello World
# Python is Fun
```
### 방법 2) \n 문자 사용 
```python
print("Hello World\nPython is Fun")
# Hello World
# Python is Fun

```
### 방법 3) """ 혹은 ''' 사용
- 따옴표 3개를 사용하여 여러 줄을 한번에 묶어 출력하는 경우에는 **꼭 위아래 여백 없이 작성하기**
```python
# 위아래 여백 주고 작성
print("""
Hello World
Python is Fun
""")
# 처음 한 줄 띄어짐
# Hello World
# Python is Fun
# 마지막 줄도 띄어짐

# 위아래 여백 없이 작성
print("""Hello World
Python is Fun""")
# Hello World
# Python is Fun
```

---
# 출력 형식
## 1. 변수 선언
### 방법 1) 변수 포맷(%d, %s, ...)과 %를 사용
-  해당 변수의 type에 해당하는 포맷을 적어주고, 맨 뒤에는 % 뒤에 변수를 나열하는 식으로 포맷 맞추기
    - 변수 포맷 : 문자열의 경우 %s를, 문자의 경우 %c를, 정수의 경우 %d, 실수의 경우 %f 등

```python
a = 5
print("A is %d" % a)

b = "apple"
print("B is %s" % b)

print("A is %d and B is %s" % (a, b))

# A is 5
# B is apple
# A is 5 and B is apple
```

### 방법 2) format 함수를 이용

- format 함수를 이용하면 직접 변수의 type을 명시하지 않더라도, 순서 혹은 이름을 명시하여 원하는 변수를 포맷에 맞춰 넣어줄 수 있음
- 숫자를 적게되는 경우에는 format 함수에 적게되는 변수에 번호를 0번부터 붙였을 때 몇 번째 값인지를 명시하기 (숫자 대신 새로운 이름을 붙여 적는 것도 가능)
-  format을 이용하는 경우에는 꼭 문자열 내 변수를 사용할 위치에 **{}**로 감싸주기
 

```python
a, b = 5, "apple"

print("A is {0}".format(a))
print("A is {new_a}".format(new_a=a))

print("B is {0}".format(b))
print("B is {new_b}".format(new_b=b))

print("A is {0} and B is {1}".format(a, b))
print("A is {new_a} and B is {new_b}".format(new_a=a, new_b=b))
print("B is {1} and A is {0}".format(a, b))
print("B is {new_b} and A is {new_a}".format(new_a=a, new_b=b))

# A is 5
# A is 5
# B is apple
# B is apple
# A is 5 and B is apple
# A is 5 and B is apple
# B is apple and A is 5
# B is apple and A is 5
```

### 방법3) f 문자열 포맷을 이용
- 별도의 함수 이용 없이 문자열 앞에 f를 붙이고 변수 이름을 중괄호{}로 감싸면 원하는 변수를 해당 위치에 넣어줄 수 있음

```python
a, b = 5, "apple"

print(f"A is {a}")
print(f"B is {b}")
print(f"A is {a} and B is {b}")

# A is 5
# B is apple
# A is 5 and B is apple
```
---
# 소수점 맞춰 출력
## 1. 소수점 맞춰 출력하기
### 방법 1) % 사용하기
```python
a = 33.567268
print("%.4f" % a)

# 소수점 4째짜리까지 값을 반올림하여 출력
# 33.5673
```

### 방법 2) format 함수를 이용하기
- 기존 포맷이 {0}이었다면 그 뒤에 :를 붙여 포맷을 지정

```python
a = 33.567268
print("{0:.4f}".format(a))

# 소수점 4째짜리까지 값을 반올림하여 출력
# 33.5673
```

### 방법 3) f 포맷을 이용
```python
a = 33.567268
print(f"{a:.4f}")

# 소수점 4째짜리까지 값을 반올림하여 출력
# 33.5673
```
---
# 다른 변수로부터 값 변경
## 1. 변수값 교체하기
```python
a, b = 5, 3
print("A is", a)

a = b
print("A is", a)

a = 2
print("B is", b)

# A is 5
# A is 3
# B is 3
```

---
# 두 변수값을 교환
## 1. 변수값 교체하기
### 방법 1) temp 이용하기

```python
a, b = 5, 3

temp = a
a = b
b = temp

print(f"A is {a} B is {b}")

# A is 3 B is 5
```

### 방법 2) ,를 이용하여 바로 교환하기

```python
a, b = 5, 3

a, b = b, a

print(f"A is {a} B is {b}")

# A is 3 B is 5
```
---
# 변수값 동시에 복사
## 1. 변수값 복사하기
- a = b = c 코드를 사용하면
- 오른쪽에서 부터 먼저 b에 값 c를 넣어주고, 그 다음 a에 값 b를 넣어주게 되므로 전부 c와 동일한 값을 갖게 됨
- a = b = c = 0 이라는 코드를 통해 a, b, c값을 동시에 전부 0으로 바꿀수도 있음

```python
a, b, c = 5, 3, 9

a = b = c

print(f"A is {a} B is {b} C is {c}")

# A is 9 B is 9 C is 9
```