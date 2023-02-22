# 백준 2167번 : 2차원 배열의 합 (https://www.acmicpc.net/problem/2167)

N, M = map(int, input().split())
arr = []

for _ in range(1, N+1):
    number = list(map(int, input().split()))
    arr.append(number)

K = int(input())

for _ in range(K):
    i, j, x, y = list(map(int, input().split()))

