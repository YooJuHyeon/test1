# SWEA 4406 : 모음이 보이지 않는 사람

T = int(input())
Vowels = ['a', 'e', 'i', 'o', 'u']
Consonants = ''

for t in range(1, T+1):
    word = input()
    words = list(word)

    for i in words:
        if i not in Vowels:        # 입력받은 알파벳 리스트의 i가 모음리스트에 없다면,
            Consonants += i        # 아무것도 없는 문자열에 i 더하기               

    print(f'#{t} {Consonants}')    # 출력 형식에 맞게 문자열 출력하고,
    Consonants = ''                # 문자열 초기화