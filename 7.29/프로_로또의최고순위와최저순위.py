def solution(lottos, win_nums):
    answer = []
    a = 0 #맞은 숫자 개수
    b = 0 #모르는숫자(0)의 개수
    c = 0
    for i in win_nums:
        for j in lottos:
            if j == i:
                a += 1

    for i in range(len(lottos)):
        if lottos[i] == 0:
            b += 1
    c = 7 - a
    if c == 7:
        c = 6
    if (a + b) == 0:
        a = 1
    answer.append(7 - (a + b))
    answer.append(c)

    return answer


lottos = [1,2,3,4,5,6]
win_nums = [7,8,9,10,11,12]
answer = solution(lottos, win_nums)
print(answer)