# 1주차 모의고사 다시 풀기

# 최빈수 구하기
# 최빈수가 여러개일때 가장 큰 값을 찾는게 어려웠음
# 이것저것 해보다가 딕셔너리 순회할때, 딕셔너리에서 최대value를 구하고 순회한 value와 비교하는 방법을 사용

T = int(input())                                # 테스트 케이스 입력받기

for _ in range(T):              
    N = int(input())                            # 테스트케이스 번호   
    numbers = list(map(int, input().split()))   # 입력받은 점수들
    my_dict = {}                                # 빈 점수 딕셔너리 생성
    mode = []                                   # 빈 최빈수 리스트 생성

    for i in numbers:                           # 입력받은 점수들 순회하기
        if i not in my_dict:                    # 만약 딕셔너리에 i가 없다면
            my_dict[i] = 1                      # 딕셔너리 key: i, value: 1
        else:                                   # 딕셔너리에 i가 있다면
            my_dict[i] += 1                     # i의 value에 1 더하기

    for key, value in my_dict.items():          # 딕셔너리 순회하기
        max_score = max(my_dict.values())       # 딕셔너리에서 최대 value 구하기

        if max_score == value:                  # (딕셔너리를 순회하면서) 최대 value와 value가 갔다면
            mode.append(key)                    # 최빈수 리스트에 key를 추가 

    print('#'+str(N), max(mode))                # #테스트케이스번호와 최빈수 리스트의 최대값 출력


# 문자열의 거울상
# if~ elif 사이사이에 continue 안 넣어도 됨
# continue는 for문 안의 if문 이후의 과정을 무시하기 위한 코드!

T = int(input())            # 테스트 케이스의 수

for t in range(1, T+1):

    word = input()
    result = ''

    for i in word:
      if i == 'b':         # for문 반복시 b가 나오면 d로 바꿔서 결과값통에 더하고 다음 반복을 실행(d, p, q도 동일하게 반복)
         result += 'd'
      elif i == 'd':
         result += 'b'
      elif i == 'p':
         result += 'q' 
      elif i == 'q':
         result += 'p'

    print(f'#{t} {result[::-1]}')   # 결과값통의 문자열을 역슬라이싱, f스트링 해서 출력 


# 신용카드 만들기 1
# 아직 반복문 돌리는게 어려운 것 같음..
# 코드 마지막에 odd = 0, even = 0으로 다시 세팅하기까지 시간이 너무 오래걸렸음

T = int(input())
odd = 0
even = 0

for i in range(1, T+1):
    numbers = list(map(int, input().split()))
    for j in range(len(numbers)):
        if j % 2 ==0:
           odd += numbers[j]*2
        else:
            even += numbers[j]

    for k in range(0, 10):
        if (odd+even+k)%10 == 0:
           print(f'#{i} {k}')
           odd = 0
           even = 0


# 신용카드 만들기 2  
# replace 메서드로 '-'없애기!!!
# len 함수로 길이조건 맞추기
# 조건 1에 해당하는 숫자를 리스트로 만들어놓고, in 문법으로 찾기
         
T = int(input())
check = [3, 4, 5, 6, 9]

for i in range(1, T+1):
    card_number = input()
    numbers = card_number.replace('-', '')      # 입력받은 카드번호에 '-'가 있다면 ''으로 바꾸기 ('-' 없애기)
    number_list = list(map(int, str(numbers)))  # 숫자를 각 자리수의 list로 바꾸기
    
    if len(number_list) == 16:                  # 만약 number_list의 길이가 16이라면 (조건2: 카드번호 숫자의 개수는 16)

        if number_list[0] in check:             # 또, number_list의 첫 번째 숫자가 check 리스트에 있다면(조건1: 카드 번호는 3, 4, 5, 6, 9 로 시작)
            print(f'#{i} 1')                    # 출력형식에 맞게 1 출력
        else:                                   # number_list의 첫 번째 숫자가 check 리스트에 없다면
            print(f'#{i} 0')                    # 0 출력

    else:                                       # 만약 number_list의 길이가 16이 아니라면
        print(f'#{i} 0')                        # 0 출력


# 소득 불균형

T = int(input())
count = 0

for x in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    average = sum(numbers) / N                 # 입력받은 소득을 합치고 N으로 나누기 (평균소득 구하기)

    for i in range(N):                         # N 만큼 반복문 돌리기
        if numbers[i] <= average:              # 입력받은 소득리스트의 i번째 숫자가 평균소득보다 작거나 같다면,
            count += 1                         # 카운트변수에 1 더하기

    print(f'#{x} {count}')                     # 출력형식에 맞게 카운트 출력
    count = 0                                  # 다음 테스트케이스를 웨해 카운트변수는 다시 0으로 초기화


# 직사각형 길이 찾기
# 직사각형은 마주보는 두 변의 길이가 같음을 이용해서 if문으로 비교해가며 풀었음

T = int(input())                                
d = 0                                           

for i in range(1, T+1):
    a, b, c = list(map(int, input().split()))

    if a == b:                                 
        d = c
    elif a == c:
        d = b
    elif b == c:
        d = a

    print(f'#{i} {d}')
    d = 0


