# SWEA 3499번 : 퍼펙트 셔플

T = int(input())
A = []                    # 카드 절반(위쪽)
B = []                    # 카드 절반(아래쪽)
shuffle = []              # 셔플한 결과값

for t in range(1, T+1):
    N = int(input())
    cards = list(input().split())
   
    if N%2 ==1:                                            # 만약 카드의 개수가 홀수일때,
        for n in range(int(len(cards)/2)+1):               # 0부터 카드절반길이+1만큼 반복문 순회
            A.insert(n, cards[n])          # 먼저놓는쪽(위쪽)리스트의 인덱스 n에 cards[n](입력받은 카드리스트의 n번째 항목)을 삽입

        for n in range(int(len(cards)/2)+1, (len(cards))):  # 카드절반길이+1부터 카드길이끝까지 순회
            B.insert(n, cards[n])                   # 아래쪽리스트의 인덱스 n에 항목 cards[n]를 삽입
    
        for i in range(int(N/2)):             # 카드의 갯수/2만큼 반복문 돌리기
            shuffle.append(A[i])              # 셔플한 결과값 리스트에 A의 i번쨰 항목 추가
            shuffle.append(B[i])              # 그 다음 셔플한 결과값 리스트에 B의 i번쨰 항목 추가
        print(f'#{t}', *shuffle, A[-1]) # 출력형식에 맞게 만든 다음, 아직 셔플리스트에 추가되지 않은 A의 마지막 항목을 같이 출력
        A = []                    
        B = []
        shuffle = []                   # 리스트 A, B, shuffle 모두 초기화

    else:               # 카드의 개수가 짝수일때는 동일하게 진행하되, 절반으로 나눈 카드 갯수가 동일하기 때문에,
        for n in range(int(len(cards)/2)):   # 카드 절반 길이만큼 반복문 순회한 후       
            A.insert(n, cards[n])

        for n in range(int(len(cards)/2), (len(cards))):
            B.insert(n, cards[n])
    
        for i in range(int(N/2)):
            shuffle.append(A[i])
            shuffle.append(B[i])
        print(f'#{t}', *shuffle)    # 셔플리스트만 출력
        A = []
        B = []
        shuffle = []
