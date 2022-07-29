a = int(input('첫번째 수를 입력하세요 : '))
b = int(input('두번째 수를 입력하세요 : '))

ai = []
bi = []
c = 0
if a == b:
    print('서로 다른 수를 입력해주세요')
    exit()

for i in range(1, a+1):
    if a % i == 0:
        ai.append(i)
for j in range(1, b+1):
    if b % j == 0:
        bi.append(j)
for k in range(0, len(ai)):
    if ai[k] in bi:
        c = ai[k]
print(f'{a}, {b}의 최대 공약수는 {c}입니다.')
