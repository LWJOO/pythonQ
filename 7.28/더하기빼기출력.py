a = int(input('+ 와 -를 번갈아 출력합니다. 몇 개를 출력할까요? : '))
for i in range(1, a+1):
    if i%2==1:
        print('+', end = '')
    else:
        print('-', end = '')
print()
