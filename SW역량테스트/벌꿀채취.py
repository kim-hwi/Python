import itertools
T = int(input())

# a = [1,2,3,4]
# b = list(map(list,itertools.combinations(a,1)))
# print(b)
for t in range(T):
    N,M,C = map(int,input().split())
    ans=[]
    arr = [[int(i) for i in input().split()] for i in range(N)]
    for k in range(N):
        maxnum = -1
        for i in range(N-M+1):
            temp = list(arr[k][i:i+M])
            # print(temp)
            for j in range(1,len(temp)+1):
                # lis = list(itertools.combinations(temp, j))
                lis = list(map(list,itertools.combinations(temp, j)))
                # print(lis,j)
                
                sumtemp = -1
                for l in lis:
                    if C>=sum(l):
                        sumtemp = 0
                        for q in l:    
                            sumtemp += q*q
                        # print(l,sumtemp)
                        maxnum=max(maxnum,sumtemp)

        ans.append(maxnum)
    ans.sort(reverse=True)
    print('#',t+1,' ',ans[0]+ans[1],sep='')
    #     for i in range(1,M+1):
    #         for j in range(N-i+1):
    #             if C>=sum(arr[k][j:j+i]):
    #                 temp = 0
    #                 for z in arr[k][j:j+i]:
    #                     temp+=z*z
    #                 maxnum=max(temp,maxnum)
    #     ans.append(maxnum)
    # ans.sort(reverse=True)
    # temp = list(itertools.combinations(arr[k], M)
    # print(ans)
    # print('#',t,' ',ans[0]+ans[1],sep='')
