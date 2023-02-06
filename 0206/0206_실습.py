# 문제 1
# 백준 10769번 : 행복한지 슬픈지
# 예제에 ':)'라는 문제 조건에 부합하지 않는 이모티콘도 있고, 이모티콘과 다른 문자가 공백 없이 붙어 있는 경우가 있어서,
# '-' 를 기준으로 그 뒤가 ')' 인지 '('인지를 확인하는 방법으로 풀이함

message = list(input())         # 한글자씩 리스트로 입력받기
happy = 0
sad = 0

for i in range(len(message)):         # 'message' 리스트 길이만큼 반복문 돌리기
    if message[i] == '-':             # i번째 문자가 - 일때,
        if message[i+1] == ')':       # 그 다음 문자(i+1)가 ) 라면,
            happy += 1                # 'happy' 변수에 1 추가
        elif message[i+1] == '(':     # 아니면 다음 문자가 ( 라면,
            sad+= 1                   # 'sad' 변수에 1 추가

if happy == sad != 0:                 # happy와 sad의 크기가 같은데, 0이 아니라면
    print('unsure')                   # unsure 출력
elif happy > sad:                     # happy가 더 크다면
    print('happy')                    # happy 출력
elif happy < sad:                     # sad가 더 크다면
    print('sad')                      # sad 출력
elif happy == sad == 0:               # happy와 sad가 0이라면 (어떤 이모티콘도 없으면)
    print('none')                     # none 출력


# 문제 2
# 백준 2455번 : 지능형 기차
count = 0                                # 역마다 열차안에 남아있는 사람의 수를 셀 변수 'count' 만들기
count_list = []                          # 역마다 열차안에 남아있는 사람의 수를 넣을 리스트 'count_list' 만들기

for i in range(4):                        # 역 개수만큼 반복문 돌리기
    off, on = map(int, input().split())   # 내린사람, 탄사람 입력받기
    get_off = count - off                 # 1. get_off = 열차안에 있는 사람 수 - 내린 사람 수
    count = get_off + on                  # 2. 열차안에 있는 사람 수 = get_off + 탄 사람 수
    count_list.append(count)              # 3. 내린사람,탄사람의 계산이 끝나면, 리스트에 열차안에 있는 사람 수 추가

print(max(count_list))                    # 리스트에서 최대값 출력


# 문제 3
# 백준 2606번 : 바이러스
# 수업때 어렴풋이 이해해서인지, 교재 참고해서 풀어도 답이 안나온다ㅠㅠ
# 왜 자꾸 타입에러가 나오는지ㅜㅜcur은 int가 아닌가
 
N = int(input())                       # 정점 개수 (컴퓨터)
M = int(input())                       # 간선 개수 (연결된 네트워크)
graph = [[] for _ in range(N+1)]
visited = [False] * (N + 1)
total = 0

for _ in range(M):                       # 인접 리스트 만들기
    c1, c2 = map(int, input().split())
    graph[c1].append(c2)
    graph[c2].append(c1)

visited = [False] * N                  # 방문 처리 리스트 만들기

def dfs(start):
    stack = [start]                    # 돌아갈 곳 기록
    visited[start] = True              # 시작 정점 방문 처리

    while stack:                       # 스텍이 빌 때까지
        cur = stack.pop                # 현재 방문 정점(스텍:후입선출)

        for adj in graph[cur]:         # 인접한 모든 정점 반복문 돌리기
            if not visited[adj]:       # 아직 방문하지 않았다면,
                visited[adj] = True    # 방문 처리하고,
                stack.append(adj)      # 스텍에 추가하기
dfs(1)                                 # 1번 정점에서 시작

cnt = 0
for i in visited:
    if i == True:
        cnt += 1

print(cnt)


# 문제 4
# 백준 4963번 : 섬의 개수
# ㅠㅠ
