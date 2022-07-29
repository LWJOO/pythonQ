a = []
for i in range(2,1001):
    b = []
    for j in range(1, i+1):
        if i%j == 0:
            b.append(j)
    if len(b) == 2:
        a.append(i)

print(f'1000까지 소수의 개수는 {len(a)}개 입니다.')
print(a)