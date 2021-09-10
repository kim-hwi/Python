def dfs (res,mon):
    if mon > 11:
        ans.append(res)
        return
    res1 = price[0]*month[mon]+res
    res2 = price[1]+res
    res3 = price[2]+res
    dfs(res1, mon+1)
    dfs(res2, mon+1)
    dfs(res3, mon+3)
    


T = int(input())
for test_case in range(1, T + 1):
    price = [int(i) for i in input().split()]
    month = [int(i) for i in input().split()]
    monthprice = [i for i in range(12)]
    ans = []
    dfs(0,0)
    print('#',test_case,' ',min(min(ans),int(price[3])),sep='')
      
