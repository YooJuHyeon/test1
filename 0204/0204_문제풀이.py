# 백준 2439번 : 별 찍기 - 2 
# 계속해서 컴파일 에러가 남
# 이것저것 알아보니까 input으로 작업한 코드가 시간초과가 났을때는, sys 입력으로 변경해주면 시간이 줄어든다는 걸 알게 됨
# 작성한 코드 위에 
# import sys
# input = sys.stdin.readline
# 를 추가하면 속도가 줄어든다고 해서 혹시나 하고 제출해보니까 pass

import sys
input = sys.stdin.readline

N = int(input())

for i in range(1,N+1):
    print(' '*(N-i)+'*'*i)


# 백준 1157번 : 단어 공부 (재도전..!)
# 딕셔너리 순회할때 중복값 조회하는게 어려웠음
# 가장 많이 등장하는 알파벳(key)를 빈 리스트에 저장해놓고, 리스트의 길이가 1 이상이면 중복값이 있다고 판단해서 풀었음
# 1주차 모의고사에서 최빈값 구하기와 비슷!

word = input().upper()          # 대문자로 입력받기
word_list = list(set(word))     # 중복 제거헤서 리스트에 저장
my_dict = {}                    # 빈 딕셔너리 만들기
mode = []                       # 빈 최빈값 리스트 만들기

for i in word_list:             # 중복 제거한 알파벳리스트 순회
    my_dict[i] = word.count(i)  # 딕셔너리에 삽입 (키=i, value=word에서 i 카운트한 값)

max_count = max(my_dict.values())   # 딕셔너리에서 최대 value 구하기

for key, value in my_dict.items():  # 딕셔너리 순회
    if max_count == value:          # 최대 value와 value가 같다면
        mode.append(key)            # 최빈값 리스트에 key를 추가

if len(mode) > 1:                   # 만약 많이 사용된 알파벳(최빈값)이 여러개라면
    print('?')                      # ? 출력
else:                               # 그게 아니라면 (최빈값리스트의 길이가 1 이하라면)
    print(*mode)                    # 최빈값리스트 언패킹해서 출력