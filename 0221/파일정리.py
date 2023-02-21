# 백준 20291번 : 파일정리 (https://www.acmicpc.net/problem/20291)
import sys
input = sys.stdin.readline

N = int(input())
my_dict = {}                     # 빈 딕셔너리 생성

for i in range(N):                    # 파일 개수만큼 반복문 돌리기
    file = input().rstrip().split('.')[1]      # file = .으로 구분해서 입력받은 리스트의 두번째 값(index=1)
    
    if file in my_dict:               # 만약 my_dict에 file이 있다면 1 더하기
        my_dict[file] += 1
    else:                             # 만약 my_dict에 file이 없다면
        my_dict[file] = 1             # my_dict의  key = file, value = 1로 설정


for key, value in sorted(my_dict.items()):   # 딕셔너리의 키-값 쌍으로 순회(with 키를 오름차순정렬해서)
    print(key, value)                        # 키-값 쌍으로 출력하기


# import sys
# input = sys.stdin.readline 쓸때 문자열이라면 문자열 마지막에 개행 문자가 포함되어 출력
# 이때 rstrip() 또는 strip() 을 써서 공백을 삭제하기!!