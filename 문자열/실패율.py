def solution(N, stages):
    answer = {}
    total = len(stages)
    for i in range(1, N+1):
        user = 0
        if stages.count(i) != 0:
            user = stages.count(i)
            answer[i] = user/total

        else:
            answer[i] = 0
        total -= user
    rs = sorted(answer, key=lambda x: answer[x], reverse=True)
    return rs
