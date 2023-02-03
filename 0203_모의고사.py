# 문제 1
# 민석이의 과제 체크하기
# 아무리 생각해도 코드에 문제가 없는데 자꾸 이상한 답이 나오고, 수정에 수정을 반복해도, 계속 똑같은 답만 나와서 오랫동안 풀었다...
# 알고보니 모의고사.py에 작성해놓고, 자꾸 python 연습장.py (연습용으로 임시로 작성해놓은 코드) 돌리고 있었음.

T = int(input())

for i in range(1,T+1):
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))
    no_submit= []

    for j in range(1, N+1):

        if j not in numbers:
            no_submit.append(j)

    print(f'#{i}', *no_submit)


# 문제 2 
# 파리 퇴치
# M크기의 파리채로 N 행렬을 순회..?
# 델타 탐색이 M*M모양의 정사각형도 되려나 싶어서, M을 2로 설정해놓고, x,y 주변을 」 모양으로 순회해보려고 했는데.. 다시보니까 좀 아닌 것 같다.

T = int(input())
dx = [0, 1, 1]   # 우, 좌하, 우하
dy = [1, 0, 1]

for _ in range(1, T+1):
    N, M = map(int, input(). split())
    matrix = [list(map(int, input(). split()))for _ in range(N)]
    death = 0
    fly = []

    for x in range(N):
        for y in range(N):

            for i in range(M):
                nx = x + dx[i]
                ny = y + dy[i]
                death += matrix[nx][ny]   

                if 0 <= nx < N and 0 <= ny < N:
                    x = nx
                    y = ny    
