a = int(input('left  수를 입력해 주세요 : '))
b = int(input('right 수를 입력해 주세요 : '))
alist = []
c = 0
for i in range(a, b+1):
    for j in range(1,i+1):
        if i%j == 0:
            alist.append(j)
    if len(alist)%2 == 0:
        c += i
    else:
        c -= i
    alist = []

print(c)
    
