# 백준 10989번 : 수 정렬하기 3 (https://www.acmicpc.net/problem/10989)
# 풀이방법 1
# 쉽게 풀었으나 메모리 초과 뜸
# 메모리 초과로 sys.stdin.readline 썼는데도 메모리초과 뜸...
 
import sys

N = int(sys.stdin.readline())
number_list = []

for _ in range(N):
    number = int(sys.stdin.readline())
    number_list.append(number)

sorted_list = sorted(number_list)

for i in range(N):
    print(sorted_list[i])

# 풀이방법 2
# sort()함수를 쓰면 메모리 초과된다고 함
# 검색을 통해 계수정렬로 풀어봤는데..완전히 이해는 안됨
# 문제는 맞았으나, 다시 풀어봐야겠음

import sys

N = int(sys.stdin.readline())
arr = [0]*10000         # 10,000개의 수를 담을 수 있는 배열 만들기
                        # (문제조건 中 "입력에는 10,000개보다 작거나 같은 자연수가 주어진다.")
for _ in range(N):
    number = int(sys.stdin.readline())
    arr[number-1] += 1  # 입력받은 수에 해당하는 인덱스에 1더하기

for i in range(10000):   # 배열 크기만큼 순회
    if arr[i] != 0:      # 값이 0이 아니라면
        for j in range(arr[i]): # 인덱스에 해당하는 숫자를 출력
            print(i+1)