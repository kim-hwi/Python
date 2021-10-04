# t,n = map(int,input().split())
# vis = [False for i in range(t)]
# board = [int(i) for i in input().split()]
# board.sort()
# ans=[]

# def solve(depth,t,n):
#     if depth == n:
#         print(' '.join(map(str,ans)))
#         return
#     for i in range(t):
#         if vis[i] != True:
#             vis[i] = True
#             ans.append(board[i])
#             solve(depth+1,t,n)
#             ans.pop()
#             vis[i] =False
# solve(0,t,n)





t, n = map(int, input().split())
board = [i for i in input().split()]
ans = []


def dfs(num, v, res):
    if len(res) == n:
        ans.append(res)
        return

    v = v.copy()
    res = res.copy()
    if v[num] != 1:
        v[num] = 1
        res.append(board[num])
        for i in range(t):
            dfs(i, v, res)


vis = [0 for i in range(t)]
r = []
for i in range(t):
    dfs(i, vis, r)
# a = set( [[1,1],[21,1]])
a = set(map(' '.join, ans))
a = list(map(int,list(a)))
a.sort()
for i in range(len(a)):
    print(a[i])
# print(sorted(a))
# a = set(''.join(ans))
# print(ans)
