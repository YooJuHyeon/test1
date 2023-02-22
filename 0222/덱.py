# 백준 10866번 : 덱 (https://www.acmicpc.net/problem/10866)
# collections deque 모듈 이용하면, 양 방향으로 삽입과 삭제가 자유로운 큐가 되기 때문에, 시간을 크게 단축

# deque.append(item)	오른쪽 끝에 새로운 원소를 삽입
# deque.appendleft(item)	왼쪽 끝에 새로운 원소를 삽입
# deque.pop()	오른쪽 끝의 원소를 제거 후 반환
# deque.popleft()	왼쪽 끝의 원소를 제거 후 반환

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
my_deq = deque()

for i in range(N):
    command = input().split()

    if command[0] == "push_front":
        my_deq.appendleft(command[1])

    elif command[0] == "push_back":
        my_deq.append(command[1])

    elif command[0] == "pop_front":
        if len(my_deq) == 0:
            print("-1")
        else:
            print(my_deq[0])
            my_deq.popleft()

    elif command[0] == "pop_back":
        if len(my_deq) == 0:
            print("-1")
        else:
            print(my_deq[-1])
            my_deq.pop()

    elif command[0] == "size":
        print(len(my_deq))

    elif command[0] == "empty":
        if len(my_deq) == 0:
            print("1")
        else:
            print("0")

    elif command[0] == "front":
        if len(my_deq) == 0:
            print("-1")
        else:
            print(my_deq[0])

    elif command[0] == "back":
        if len(my_deq) == 0:
            print("-1")
        else:
            print(my_deq[-1])