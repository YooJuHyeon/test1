# 문제1
# 백준 1547번 : 공 (https://www.acmicpc.net/problem/1547)
# 풀이방법 1 - 처음에 insert 메서드 썼다가 리스트에 게속 추가되어서 실패 > index 메서드로 X,Y 위치 지정해주고, 위치 바꿈
# 풀이방법 2 - 리스트[X]와 리스트[Y]의 위치를 바꿨으나 list index out of range라는 index에러가 나서, 리스트에 0 추가함
# 풀이방법 2 - 리스트를 [0, 1, 0, 0]으로 만들어도 알아보기 쉬울 것 같음

# 풀이방법 1 - X컵과 Y컵의 위치를 바꾸기
N = int(input())                         # 컵의 위치를 바꾼 횟수
cup = [1, 2, 3]                          # 세 개의 컵 리스트

for _ in range(N):
    X, Y = map(int, input().split())
    X1 = cup.index(X)                    # X1 = X의 인덱스
    Y1 = cup.index(Y)                    # Y1 = Y의 인덱스 
    cup[X1], cup[Y1] = cup[Y1], cup[X1]  # X컵과 X컵의 위치 바꾸기(인덱스 바꾸기)

print(cup[0])                            # 첫번째 위치(공이 있는)에 있는 컵의 번호 출력


# 풀이방법 2 
M = int(input())                        # 컵의 위치를 바꾼 횟수
cup = [0, 1, 2, 3]                      # 세 개의 컵 리스트

for _ in range(M):                   
    X, Y = map(int, input().split())
    cup[X], cup[Y] = cup[Y], cup[X]     # X번째 요소값과 Y번째 요소값을 서로 바꿔주기

print(cup.index(1))                     # 1의 위치 출력


# 문제2
# 백준 5576번 : 콘테스트 (https://www.acmicpc.net/problem/5576)

W_score = []                         # 빈 W대학의 점수 리스트
K_score = []                         # 빈 K대학의 점수 리스트

for _ in range(10):
    W = int(input())                 # 반복문 10번 돌리기 - 입력받은 수들을 W대학리스트에 추가
    W_score.append(W)

for _ in range(10):
    K = int(input())                 # 반복문 10번 돌리기 - 입력받은 수들을 K대학리스트에 추가
    K_score.append(K)

print(sum(sorted(W_score)[7:]), sum(sorted(K_score)[7:])) # W대학,K대학 점수리스트를 오름차순으로 정렬하고, 7번째부터 마지막까지 슬라이싱한 것의 합을 차례로 출력


# 문제3
# 백준 2846번 : 오르막길 (https://www.acmicpc.net/problem/2846)

# 1. 실습시간에는 무조건 오르막길 끝 높이 - 오르막길 시작 높이 으로 높이 계산 하려고 했는데, 
# 다른분들의 풀이를 보고 오르막길이라면, 앞길 높이 - 뒷길 높이 해서 빈통에 계속해서 더해나가도 오르막길 높이를 구할 수 있음을 알았다.
# 2. 

N = int(input())
numbers = list(map(int, input().split()))
temp = 0                                 # 오르막길 높이 저장할 변수
uphill_road = []                         # 최종 오르막길 높이 N개 담을 리스트

for i in range(1, N):                  
    if numbers[i] > numbers[i-1]:        # 뒷길 높이가 앞길높이보다 크다면, (오르막길)
        temp += numbers[i] - numbers[i-1] # 두 길의 높이차를 temp 변수에 더해준다.
        if i == N-1:                      # 오르막길인데 길이 끝난다면, 
            uphill_road.append(temp)      # 오르막길 리스트에 temp값을 추가한다.
    
    else:                                 # 만약 오르막길이 아닌 경우라면,
        uphill_road.append(temp)          # 지금까지의 temp값을 오르막길 리스트에 추가한다.
        temp = 0                          # 그리고 다시 temp는 0으로 초기화

print(max(uphill_road))                   # 오르막길 높이 리스트의 최대값을 출력 