print('리스트 구분은 띄어쓰기로 합니다. ')
x = list(input('리스트를 입력하세요 : ').split())

def seq_search_sentinel(a, key):
    b = a.copy()
    b.append(key)
    i = 0
    while True:
        if b[i] == key:
            break
        i += 1
    if i == len(a):
        return -1
    else:
        return i

def max_of(a):
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum

y = max_of(x)
index = seq_search_sentinel(x, y)
print(f'최댓값은 {y}입니다.')
if index == -1:
    print('검색값을 갖는 원소가 존재하지 않습니다.')
else:
    print(f'최댓값은 a[{index}]에 있습니다.')