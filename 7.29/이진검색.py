def bin_search(a, key):
    pl = 0
    pr = len(a)-1

    while True:
        pc = (pr+pl)//2
        if a[pc] == key: 
            return pc
            break #a[pc] 와 key가 일치하는 경우
        elif a[pc] > key:
            pr = pc - 1
        else:
            pl = pc + 1
        if pl > pr:
            return -1
            break #검색 범위가 더 이상 없는 경우

print('리스트 구분은 띄어쓰기로 합니다. 중복x, 오름차순 정렬로 입력')
x = list(map(int, input('리스트를 입력하세요 : ').split()))
y = int(input('어떤 수를 찾으시나요? : '))

answer = bin_search(x, y)
if answer == -1:
    print('검색한 숫자가 없습니다.')
else:
    print(f'검색값은 리스트[{answer}]에 있습니다.')