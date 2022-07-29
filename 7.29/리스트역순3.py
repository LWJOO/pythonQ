print('리스트 구분은 띄어쓰기로 합니다.')
x = list(input('리스트를 입력하세요 : ').split())

def reverse_list(a):
    n = len(a)
    for i in range(n // 2):
        a[i], a[n - i - 1] = a[n - i - 1], a[i]

reverse_list(x)
print(x)