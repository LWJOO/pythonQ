def solution(n, s):
    answer = []
    a = []
    b = 0
    for i in range(1, s//2+1):
        for j in range(s,1,-1):
            if (i + j) == s:
                answer.append([i,j])

    for i in range(len(answer)):
        a.append(answer[i][0] * answer[i][1])
    
    for i in range(len(a)):
        if a[i] > b:
            b, c = a[i], i 
    if s < 2:
        return [-1]
    else:
        d = answer[c]
        return d

n = 2
s = 8
answer = solution(n, s)
print(answer)