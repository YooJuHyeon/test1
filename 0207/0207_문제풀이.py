# 문제1
# 백준 10814번 : 나이순 정렬
# 딕셔너리로 풀려고 했었음
# key에 나이를 넣으면 중복값이 제거되고, 나이를 value에 넣으면 정렬하기가 복잡해지고..
# 결국 구글링했는데, 대부분이 람다 함수로 풀었다.
# 난 아직 람다함수를 잘 모르기에 람다함수 없이 푸는 풀이를 찾았는데,
# 리스트에 추가할때 i를 넣으니, 나이가 같을때 먼저 가입한 사람순으로 출력 가능했다.

N = int(input())   
members = []                   # 가입한 사람들의 정보 리스트

for i in range(N):
    A, B = input().split()

    members.append([int(A), i, B])     # 리스트에 [나이, i, 이름] 형태로 추가

sorted_members = sorted(members)       # 오름차순 정렬

for j in range(N):
    print(sorted_members[j][0], sorted_members[j][2])     # i 빼고 출력
                                                          # 결국엔 이차원리스트 행렬에서 i가 포함된 1렬 빼고 출력함