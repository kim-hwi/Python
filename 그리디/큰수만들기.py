from collections import deque


def solution(number, k):
    if len(number) == 1 and k == 1:
        return ''
    num = list(number)
    answer = deque()
    answer.append(num[0])
    now = 0
    for i in range(1, len(num)):
        if answer[-1] < num[i] and now < k:
            while answer[-1] < num[i] and now < k:
                answer.pop()
                now += 1
                if len(answer) == 0:
                    break
            answer.append(num[i])
        else:
            answer.append(num[i])
    answer = list(answer)
    return ''.join(answer)[:len(num)-k]
