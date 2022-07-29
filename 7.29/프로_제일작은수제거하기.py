def solution(arr):
    a = 0
    if len(arr) > 1:
        for i in range(1,len(arr)):
            if arr[i-1] > arr[i]:
                a = arr[i]
        arr.remove(a)
        return arr
    else:
        return [-1]