print('리스트를 역순으로 출력합니다.')
n=int(input('원소 수를 입력하세요 : '))
x = []

for i in range(n):
    s = input(f'x[{i}]값을 입력하세요 : ')
    x.append(int(s))

def reverse_list(a):
    n = len(a)
    for i in range(n // 2):
        a[i], a[n - i - 1] = a[n - i - 1], a[i]

reverse_list(x)
print('리스트를 역순으로 출력합니다.')
for i in range(n):
    print(f'x[{i}]={x[i]}')