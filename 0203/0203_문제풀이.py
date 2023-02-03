# 백준 2884번 : 알람 시계 

# 백준 2525번(오븐시계)와 비슷했던 문제이다.
# 다만 오븐시계는 시간을 더하는 조건에 더할 시간이 변수였다면, 알람시계는 시간을 빼는 조건에 뺄 시간이 정해져 있다.
# 때문에 오븐시계 문제는 시간단위가 바뀔경우 몫과 나머지를 이용해 시와 분을 계산했었다면,
# 이 문제는 시간단위가 바뀔 경우 단순히 M + 15(60-45)를 해주고, H가 0일때는 23으로 바꿔주었다.

H, M = map(int,input().split())

if M >= 45:                           # 설정한 알람 시각의 분이 45 이상이라면 분-45만 계산해서 출력
    print(H, M-45)

else:                                 # 설정한 알람 시각의 분이 45 이하이고,
    if H == 0:                        # 시간이 0시라면,
        print(23, M+15)               # 시간을 23으로 바꿔주고, 분에 15를 더해 출력
    else:                             # 시간이 0시가 아니라면
        print(H-1, M+15)              # 시간-1, 분+15 출력


# 백준 1152번 : 단어의 개수

words = list(input().split())

print(len(words))


# 백준 1157번 : 단어 공부
# 딕셔너리로 풀려고 했는데, 딕셔너리 순회가 어려워서 막혔음.. 다시풀기

word = input().upper()          # 대문자로 입력받기
word_list = list(set(word))     # 중복 제거헤서 리스트에 저장
my_dict = {}                    # 빈 딕셔너리 만들기
max = 0

for i in word_list:             # 중복 제거한 알파벳리스트 순회
    my_dict[i] = word.count(i)  # 딕셔너리에 삽입 (키=i, value=word에서 i 카운트한 값)

for key, value in count_dict.items(): 
    if max < value:
        max = value
        mode = key

print(mode)