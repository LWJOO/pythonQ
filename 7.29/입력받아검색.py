print('리스트 구분은 띄어쓰기로 합니다. ')
x = list(input('리스트를 입력하세요 : ').split())
y = input('어떤 수를 찾으시나요? : ')

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

index = seq_search_sentinel(x, y)

if index == -1:
    print('검색값을 갖는 원소가 존재하지 않습니다.')
else:
    print(f'검색값은 a[{index}]에 있습니다.')