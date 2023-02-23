# 백준 2167번 : 2차원 배열의 합 (https://www.acmicpc.net/problem/2167)
# pypy로 제출할때는 맞았는데.. python으로 제출하면 시간초과.. 3중 for문 때문인듯
# 변수 이름 sum으로 짓지 말기!!

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []

# 배열 N의 크기만큼 반복문 돌려서 M개의 정수를 리스트로 입력받고, 리스트를 arr라는 리스트에 추가(이차원 리스트)
for _ in range(N):
    number = list(map(int, input().split()))
    arr.append(number)                       

K = int(input())
sum = 0

# K번(입력줄수) 반복문 돌리고, 네 개의 정수 입력받기
for _ in range(K):
    i, j, x, y = list(map(int, input().split()))

# 행 i부터 행 x+1(인덱스떄문에 +1)까지 반복문, 열 j부터 열 y까지 반복문 돌려서 순회하면서 sum에 더하기 (이차원 리스트 순회)
    for a in range(i, x+1):
        for b in range(j, y+1):

# arr의 인덱스는 0부터 시작하기 때문에 각각의 좌표에 -1 해줌
            sum += arr[a-1][b-1]     

#  이차원리스트순회가 끝나면 sum을 출력하고, sum의 값 초기화 (K번 반복)
    print(sum)
    sum = 0

