# 문제 1 
# 백준 17608번 : 막대기
# 풀이방법 1 - 틀렸습니다.
import sys
input = sys.stdin.readline 

N = int(input())
stack = []
cnt = 1

for _ in range(N):
    number = int(input())
    stack.append(number)

last_stick = stack[-1]

for i in range(N-1, 0, -1):
    if last_stick < stack[i]:
            cnt += 1
            last_stick = stack[i]

print(cnt)

# 풀이방법 2 
# 첫번째 풀이방법에서의 역슬라이싱 대신 pop 이용

import sys
input = sys.stdin.readline 

N = int(input())
stack = []
cnt = 1                      # 마지막 막대기의 값은 1로 카운트 해놓기

for _ in range(N):         
    number = int(input()) 
    stack.append(number)     # 인풋 받은 순서대로 stack에 추가

high = stack.pop()           # 비교할 더 높은 막대기 설정 = 스택에서 pop한 값 (물론 처음엔 더 높은막대기가 아니라 마지막 막대기로 셋팅)
for i in range(N-1):         # 범위 1 줄여서 반복문 돌리기(위에 pop 했으니까?) 
    last = stack.pop()       # 마지막 막대기 = 스택에서 pop (현재 스택의 맨 끝)

    if last > high:          # last(스택의 맨 끝)가 high보다 높다면
        cnt +=1              # 카운트에 1 더하고,
        high = last          # high를 last로 바꾸기
        
print(cnt)


# 문제 2
# 백준 7568번 : 덩치
# 너무 모르겠어서 팀원분의 코드를 보고, 그림을 그려보니까 넘 이해가 잘 됐다.
# 이차원 리스트는 이렇게 푸는거구나...수업시간에 배운 개념을 이렇게 써먹는구나..

N = int(input())
rank_list = []    
rank = [1]*N                           # 랭킹 점수 리스트 모두 1로 셋팅

for i in range(N):
    kg, cm = map(int,input().split())
    rank_list.append([kg, cm])              # 입력받은 키와 몸무게를 이차원리스트 형태로 추가

for i in range(N):
    for j in range(N):              # 행렬 순회

        # 이전 리스트[i행] 몸무게[0열]보다 다음리스트[j행]의 몸무게보다 크고, 
        # 이전리스트보다 다음 리스트의 키[1열]가 크다면
        if rank_list[i][0] < rank_list[j][0] and rank_list[i][1] < rank_list[j][1]:
            rank[i] += 1        # 랭크리스트 인덱스 i에 1 더하기

print(*rank)