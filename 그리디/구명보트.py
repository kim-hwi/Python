from collections import deque


def solution(people, limit):
    people.sort()
    p = deque(people)
    answer = 0
    while len(p) != 0:
        l = p.pop()
        answer += 1
        if len(p) == 0:
            break
        if p[0]+l <= limit:
            p.popleft()
    return answer
