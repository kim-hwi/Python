def solution(begin, target, words):
    global word
    word = words
    global vis
    vis = [0 for i in range(len(words))]
    global tar
    tar = target
    global res
    res = []
    answer = 0
    dfs(0, begin)
    if len(res) == 0:
        return 0
    print(res)
    return min(res)


def dfs(depth, now):
    if now == tar:
        res.append(depth)
        return
    if depth == len(word):
        return
    for i in range(len(word)):
        num = 0
        for j in range(len(now)):
            if word[i][j] != now[j]:
                num += 1
        if num == 1 and vis[i] == 0:
            # print(word[i],now)
            vis[i] = 1
            dfs(depth+1, word[i])
            vis[i] = 0
