# 코드업 6096번 : 바둑알 십자 뒤집기
# 이차원 리스트는 역시 어려운 게 맞구나..
# 게다가 == 와 = 연산자의 차이를 이해하지 못하고, ==로만 코드를 작성해서 계속 틀렸다...
# =는 할당 연산자, ==는 비교연산자!!!


# 리스트 컴프리헨션으로 빈 바둑판 만들기
checkerboard = [[]*19 for _ in range(19)]

# 19행만큼 반복문 돌려서 바둑알 입력받기
for i in range(19):
    checkerboard[i] = list(map(int, input().split()))


n = int(input())
# 뒤집기 횟수만큼 반복문 돌리기
for j in range(n):
    x,y = map(int, input().split())

    for k in range(19):                   
        if checkerboard[x-1][k] == 1:     # 바둑판의 x행,k열이 1이라면, 0으로 바꿔주기 (가로순회)
            checkerboard[x-1][k] = 0
        else:                             # 아니면, 1로 바꿔주기
            checkerboard[x-1][k] = 1
      
        if checkerboard[k][y-1] == 1:     # 바둑판의 k행 y열이 1이라면, 0으로 바꿔주기(세로순회)
            checkerboard[k][y-1] = 0
        else:                             # 아니면, 1로 바꿔주기
           checkerboard[k][y-1] = 1

for a in range(19):                           # 이차원리스트 순회하며, 출력하기
    for b in range(19):
        print(checkerboard[a][b], end=' ')
    print()