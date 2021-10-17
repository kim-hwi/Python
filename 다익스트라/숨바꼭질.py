from heapq import heappush, heappop
n,m=map(int,input().split())

# s = [[] for i in range(n + 1)]
dic={i+1:[] for i in range(n+1)}
# dic[1].append(1)

for i in range(m):
    a, b = map(int, input().split())
    dic[a].append([b,1])
    dic[b].append([a,1])
# print(dic)


def di (start):
    heap=[]
    heappush(heap,[0,start])
    dp = [10000000 for i in range(n+1)]
    dp[start] = 0
    while heap:
        we,loc = heappop(heap)
        for n_loc,n_we in dic[loc]:
            wie = we+n_we
            if wie<dp[n_loc]:
                dp[n_loc] = wie
                heappush(heap,[wie,n_loc])
    return dp


# 딕셔너리를 이용한 풀이 -> 노드가 번호가 아니더라도 풀 수가 있다.
def dij (start): 
    heap=[]
    heappush(heap,[0,start])
    dp = [100000000 for i in range(n+1)]
    dp[start] = 0
    while heap:
        we, loc=heappop(heap)
        for n_loc,n_we in dic[loc]:
            wie = we+n_we
            if dp[n_loc]>wie:
                dp[n_loc] = wie
                heappush(heap,[wie,n_loc])
    return dp

# 리스트를 이용한 풀이

# def dij (start):
#     heap=[]
#     heappush(heap,[0,start])
#     dp = [100000000 for i in range(n + 1)]
#     dp[start] = 0
#     while heap:
#         we,nu=heappop(heap)
#         for n_nu, n_we in s[nu]:
#             wei = we + n_we
#             if dp[n_nu] > wei:
#                 dp[n_nu] = wei
#                 heappush(heap, [wei, n_nu])
#     return dp

dp=di(1)
max_dp = max(dp[1:])
print(dp.index(max_dp), max_dp, dp.count(max_dp))

dic = {i:[] for i in range(n+1)}



