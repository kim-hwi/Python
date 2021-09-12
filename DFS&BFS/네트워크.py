def solution(n, computers):
    global N
    global computer
    global vis
    count = 0
    vis = [0 for i in range(n)]
    N = n
    computer = computers
    for i in range(n):
        if vis[i] != 1:
            dfs(i)
            count += 1
    # print(vis,count)
    return count


def dfs(coms):
    vis[coms] = 1
    for i in range(N):
        if computer[coms][i] == 1 and vis[i] != 1:
            dfs(i)
