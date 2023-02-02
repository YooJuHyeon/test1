# 백준 2908번 : 상수 (https://www.acmicpc.net/problem/2908)

# 풀이방법 1 
A, B = input().split()                   # 문자열로 A, B 입력받기
numbers = [int(A[::-1]), int(B[::-1])]   # A,B를 리스트에 넣고, 각각 문자열 역슬라이싱, 정수로 변환

print(max(numbers))                      # 리스트에서 최대값 출력

# 풀이방법 2
A, B = input().split()                   # 문자열로 A, B 입력받기

if int(A[::-1]) > int(B[::-1]):          # 역슬라이싱한 문자열A를 정수화한것이 역슬라이싱한 문자열B를 정수화한것보다 크다면
    print(int(A[::-1]))                  # A 출력

else:                                    # 아니면
    print((B[::-1]))                     # B 출력


# 백준 2742번 : 기찍 N (https://www.acmicpc.net/problem/2742)

# 풀이방법 1
N = int(input())                  

for i in range(N, 0, -1):             # 범위 N부터 0까지(1 작게) 1씩 감소하면서 반복
    print(i)                          # i 출력

# 풀이방법 2
N = int(input())

for i in range(N):                   # N번 반복
    print(N-i)                       # 반복하면서 N-i 출력 (i는 0,1,2..N-1까지일테니까)


# 백준 1546번 : 평균 (https://www.acmicpc.net/problem/1546)    

# 풀이방법 1
N = int(input())
score = list(map(int, input().split()))
max_score = max(score)
new_score = []

for i in score:
    new_score.append(i/max_score*100)       # 반복문 돌면서 i/최댓값*100을 새 리스트에 추가

print(sum(new_score)/len(new_score))        # 새 리스트의 합을 새 리스트의 길이로 나눠서 출력

# 풀이방법 2
# 풀이방법 1에서 굳이 new_score라는 새 리스트를 만들 필요가 없어보여서 score의 scores[i]항목을 바꿔줌

N = int(input())
score = list(map(int, input().split()))
max_score = max(score)

for i in range(N):
    score[i] =score[i]/max_score*100

print(sum(score)/len(score))