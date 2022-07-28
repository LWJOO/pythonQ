a = int(input('첫번째 수를 입력하세요 : '))
b = int(input('두번째 수를 입력하세요 : '))
c = 0
if a == b:
    print('서로 다른 정수를 입력해주세요')
    exit()

for i in range(1, b+1):
    if a * i % b == 0:
        c = a * i
        break

print(f'{a}, {b}의 최소공배수는 {c}입니다.')
