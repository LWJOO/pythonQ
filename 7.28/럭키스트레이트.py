a = input('점수를 입력해 주세요 : ')
alist = list(map(int, str(a)))
al = int(len(alist)/2)
b = 0
c = 0
if len(alist)%2 == 0:
    for i in range(0, al):
        b += alist[i]
        c += alist[i + al]
    if b == c:
        print('LUCKY')
    else:
        print('READY')

else:
    print('READY')
