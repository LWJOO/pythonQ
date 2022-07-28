a = int(input('수를 입력하세요 : '))
b = 0
for i in range(a):
    if a == i*i:
        print((i+1)*(i+1))
        b = 1
if b == 0:
    print(-1)