root = int(input('값을 입력하세요 : '))
k=0
for i in range(2,root):
    for j in range(2, 6):
        if i**j == root:
            print(f'{i}^{j}={root}')
            k += 1
if k == 0:
    print('결과 없음')
