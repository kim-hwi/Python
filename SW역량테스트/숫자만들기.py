def dfs(temp,temp2):
    global ans
    # print(temp,temp2)
    if sum(temp) == 0:
        ans.append(temp2)
    for i in range(4):
        arr = temp.copy()
        lis = temp2.copy()
        if arr[i]>0:
            arr[i]-=1
            if i == 0:
                lis.append('+')
            if i == 1:
                lis.append('-')
            if i == 2:
                lis.append('*')
            if i == 3:
                lis.append('/')
            dfs(arr,lis)

# def dfs (temp,temp2):
#     # print(temp,temp2)
#     global ans
#     if sum(temp) == 0:
#         ans.append(temp2)
#     arr1 = temp.copy()
#     arr2 = temp.copy()
#     arr3 = temp.copy()
#     arr4 = temp.copy()
#     lis1 = temp2.copy()
#     lis2 = temp2.copy()
#     lis3 = temp2.copy()
#     lis4 = temp2.copy()
#     if arr1[0]>0:
#         arr1[0]-=1
#         lis1.append('+')
#         dfs(arr1,lis1)
#     if arr2[1] > 0:
#         arr2[1] -= 1
#         lis2.append('-')
#         dfs(arr2,lis2)
#     if arr3[2] > 0:
#         arr3[2] -= 1
#         lis3.append('*')
#         dfs(arr3,lis3)
#     if arr4[3] > 0:
#         arr4[3] -= 1
#         lis4.append('/')
#         dfs(arr4,lis4)


T = int(input())

for t in range(T):
    N = int(input())
    un = list(map(int,input().split()))
    num = list(map(int, input().split()))
    un2 = []
    ans = []
    answer =[]
    dfs(un,[])
  
    for te in ans:
        res = num[0]
       
        for l in range(N-1):
           
            if te[l] == '+':
                res = res+num[l+1]
            elif te[l] == '-':
                res = res-num[l+1]
            elif te[l] == '*':
                res = res*num[l+1]
            elif te[l] == '/':
                res = int(res/num[l+1])
       
        answer.append(res)

    print('#',t+1,' ',abs( max(answer) - min(answer) ),sep='')

