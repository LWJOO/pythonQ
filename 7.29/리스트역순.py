print('리스트의 최댓값을 구합니다.')
print('주의: "End"를 입력하면 원소 입력을 종료합니다.')
i = 0
x = []

def reverse_list(a):
    n = len(a)
    for i in range(n // 2):
        a[i], a[n - i - 1] = a[n - i - 1], a[i]

while True:
    s = input(f'x[{i}]값을 입력하세요.: ')
    if s == 'End':
        break
    x.append(int(s))
    i += 1

reverse_list(x)
print(x)