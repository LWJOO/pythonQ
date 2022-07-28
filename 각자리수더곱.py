a = input('수를 입력해 주세요 : ')
b = 0
alist = list(map(int, str(a)))
for i in range(0, len(alist)):
    if alist[i] == 0 or alist[i] == 1:
        b += int(alist[i])
    else:
        if b ==0:
            b += int(alist[i])
        else:
            b *= int(alist[i])
print(b)
