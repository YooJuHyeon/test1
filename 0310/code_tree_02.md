![](https://velog.velcdn.com/images/dbwnwngus/post/3559f8cc-3700-4c1d-8e50-3a8dd0785342/image.png)

## split()함수 사용

 - 공백을 기준으로 문자열을 잘라 각 _잘려나간 단위가 하나의 원소가 되어_ 해당 원소들을 가지고 있는 하나의 **list**가 만들어짐
```python
a = input()
print(a.split())

>> 13 17
['13', '17']
```
---
### 1. split()함수와 list index 이용해보기
```python
arr = input().split()
n = int(arr[0])
m = int(arr[1])

print(n)
print(m)
print(n * m)

>> 13 17

13
17
221
```
---
### 2. 특정 문자를 사이에 두고 2개의 값을 입력
```python
a = input()
print(a.split(":"))

>> 50:60

['50', '60']
```