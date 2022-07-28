a = input('0에서 99 사이 수를 입력하세요 : ')
a = a.zfill(2)
alist = list(map(int, str(a)))
blist = list(alist)
i = 1
while True:
    b = alist[0] + alist[1]
    bli = list(map(int, str(b)))
    alist[0] = alist[1]
    alist[1] = bli[-1]
    bli = []
    if alist == blist:
        print(f'{i}번')
        break
    else:
        i += 1
    