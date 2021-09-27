T = int(input())

for t in range(T):
    N,M,C = map(int,input().split())
    ans=[]
    arr = [[int(i) for i in input().split()] for i in range(N)]
    for k in range(N):
        maxnum=-1
        for i in range(1,M+1):
            for j in range(N-i+1):
                if C>=sum(arr[k][j:j+i]):
                    temp = 0
                    for z in arr[k][j:j+i]:
                        temp+=z*z
                    maxnum=max(temp,maxnum)
        ans.append(maxnum)
    ans.sort(reverse=True)
    print(ans)
    # print('#',t,' ',ans[0]+ans[1],sep='')