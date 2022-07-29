def seq_search(a, key):
    i = 0
    j = 0
    while True:
        if i == len(a):
            return -1, j
        j += 1
        if a[i] == key:
            return i, j
        j += 1
        i += 1

def seq_search_sentinel(a, key):
    b = a.copy()
    b.append(key)
    i = 0
    j = 0
    while True:
        if b[i] == key:
            break
        i += 1
        j += 1
    if i == len(a):
        return -1, j
    else:
        return i, j

a = [2, 5, 1, 3, 9, 6, 7]
x = int(input('검색할 숫자를 입력하세요 : '))

index1, if1 = seq_search(a, x)
index2, if2 = seq_search_sentinel(a, x)

if index1 == -1:
    if1 += 1
    print('검색값을 갖는 원소가 존재하지 않습니다.')
else:
    if1 += 1
    print(f'(선형검색)검색값은 a[{index1}]에 있습니다.')
print(f'if를 {if1}번 사용했습니다.')

if index2 == -1:
    if2 += 1
    print('검색값을 갖는 원소가 존재하지 않습니다.')
else:
    if2 += 1
    print(f'(보초법)검색값은 a[{index2}]에 있습니다.')
print(f'if를 {if2}번 사용했습니다.')