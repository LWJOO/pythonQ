arr = [1,2,3]
a = arr.copy()
c = 0
for i in range(len(arr)-1):
    b = arr[i+1]
    for j in range(1, b+1):
        if arr[i] * j % arr[i+1] == 0:
            c = arr[i] * j
            arr[i+1] = c
            print(c)
            break
for k in range(len(a)):
    print(f'{a[k]}',end = ' ')
print(f'의 최소공배수는 {c}입니다.')