N, X = map(int, input('리스트의 크기와 크기를 비교할 수를 입력하세요 : ').split())
A = list(map(int, input(f'{N}개짜리 리스트를 입력하세요 : ').split()))
answer = []
if len(A) != N:
    print('잘못된 크기의 리스트가 입력되었습니다.')
    exit()

for i in A:
    if i < X:
        answer.append(i)

for i in answer:
    print(i, end = ' ')
    print()
