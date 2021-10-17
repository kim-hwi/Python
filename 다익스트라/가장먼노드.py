from heapq import heappop, heappush

dic = {i: [] for i in range(30000)}


def dij(start):
    global dic
    dp = [100000 for i in range(30000)]
    dp[start] = 0
    heap = []
    heappush(heap, [dp[start], start])
    while heap:
        we, loc = heappop(heap)
        for n_loc, n_we in dic[loc]:
            wei = we+n_we
            if wei < dp[n_loc]:
                dp[n_loc] = wei
                heappush(heap, [wei, n_loc])
    for i in range(30000):
        if dp[i] == 100000:
            dp[i] = -1
    return dp


def solution(n, edge):
    global dic
    for e in edge:
        dic[e[0]].append([e[1], 1])
        dic[e[1]].append([e[0], 1])
    dp = dij(1)
    num = max(dp)
    answer = 0
    for i in dp:
        if i == num:
            answer += 1
    print(answer)
    # dij(1)

    return answer
