# CodeUp 6092번 : 이상한 출석 번호 부르기1
# point : 빈 리스트를 0으로 채워넣고, 인풋값들 순회하면서 1씩 더하기!!

N = int(input())
numbers = list(map(int, input().split()))  # 출석 부른 번호 리스트
students = [0]* 23     # 0이 23개(학생수) 있는 리스트 만들기

for i in numbers:          # 출석번호 리스트 순회하면서,
    students[i-1] += 1     # students 리스트 i-1(리스트는 0부터 시작하니까..) 에 1 더하기

print(*students)           # 완성된 students 리스트를 언패킹해서 출력


# CodeUp 6093번 : 이상한 출석 번호 부르기2
N = int(input())
numbers = list(map(int, input().split()))  # 출석 부른 번호 리스트
reversed_number = numbers[::-1]            # 리스트 역슬라이싱하기

print(*reversed_number)                    # 역슬라이싱된 리스트를 언패킹해서 출력


# CodeUp 6094번 : 이상한 출석 번호 부르기3

N = int(input())

numbers = list(map(int, input().split()))

print(min(numbers))                        # 입력받은 리스트에서 최소값 출력