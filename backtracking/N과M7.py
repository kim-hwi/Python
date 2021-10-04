n, t = map(int, input().split())
L = list(map(int, input().split()))
L.sort()
ans = []
# print(L)


def dfs(depth, n, t):
    if depth == t:
        print(' '.join(map(str, ans)))
        return
    for i in range(n):
        ans.append(L[i])
        dfs(depth+1, n, t)
        ans.pop()
       


dfs(0, n, t)
