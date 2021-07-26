N, M = map(int, input().split())
vist = [False for i in range(N)]
res = [0]


def dfs(depth, N, M):
  if M+1 == depth:
    for i in range(1, M+1):
      print(res[i], end=' ')
    print()
    return
  for j in range(N):
    if res[-1] <= j+1:
      res.append(j+1)
      dfs(depth+1, N, M)
      res.pop()


dfs(1, N, M)
