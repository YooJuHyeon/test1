# CodeUp 6097 : 설탕과자 뽑기
# 틀려서, 간단히 행과 열 순서만 바꿔주니 맞았음
# 생각해보니 문제에서 세로라고 해서 반드시 열, 가로라고 해서 행이 아님
# 오히려 그림을 그려보면 세로가 행, 가로가 열!
# 이래서 행과 열에 대한 나만의 기준을 잘 잡아야 하는구나..

h, w = map(int, input().split())

# 0으로만 이루어진 이차원 리스트 만들기 (리스트 컴프리헨션)
checkerboard = [[0] * w for _ in range(h)]   

n = int(input())

# 막대의 개수만큼 반복
for _ in range(n):
    l, d, x, y = map(int, input().split())
    
    # 막대의 길이만큼 1로 바꿔주기 위해서 반복문
    for a in range(l):

        # 만약 방향이 가로라면(d==0), 행은 그대로 두고, 열만 막대의 길이만큼 이동하면서(반복문) 1로 바꿔주기 
        if d == 0:
            checkerboard[x-1][y-1+a] = 1

        # 만약 방향이 세로라면(d==1), 열은 그대로 두고, 행만 막대의 길이만큼 이동하면서(반복문) 1로 바꿔주기 
        elif d == 1:
            checkerboard[x-1+a][y-1] = 1

# 막대가 그려진 이차원 리스트를 순회하면서 출력
for i in range(h):
    for j in range(w):
        print(checkerboard[i][j], end=' ')
    print()
