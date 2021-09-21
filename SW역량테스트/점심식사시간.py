import itertools
T = int(input())
ans=[]
pnum=0
r=[]
def dfs(n,arrtemp):
    
    global arr
    global pnum
    if n== pnum:
        r.append(arrtemp)
        return
    print(arr[n])
    arr1=arrtemp.copy()
    arr2=arrtemp.copy()
    arr1.append(['A',arr[n][0]])
    dfs(n+1, arr1)
    arr2.append(['B',arr[n][1]])
    dfs(n+1, arr2)


for t in range(T):
    n = int(input())
    board = [[int(i) for i in input().split(' ')]for j in range(n)]
    ex=[]
    arr=[]
    for i in range(n):
        for j in range(n):
            if board[i][j] > 1:
                ex.append([i,j,board[i][j]])
                board[i][j] = 0
                
    
    
    for i in range(n):
        for j in range(n):
            if board[i][j] ==1:
                pnum+=1
                arr.append([abs(i-ex[0][0])+abs(j-ex[0][1]),abs(i-ex[1][0])+abs(j-ex[1][1])])
                # arr.append(['B',abs(i-ex[1][0])+abs(j-ex[1][1])])
                print('A',abs(i-ex[0][0])+abs(j-ex[0][1]))
                print('B',abs(i-ex[1][0])+abs(j-ex[1][1]))
    
    print(arr)
    # print(ex)    
    dfs(0,[])
    
    # for i in range(n):
    r.sort()
    print(r)   
    for i in r:
        A=[]
        A2=[]
        B=[]
        B2=[]
        for j in i:
            if j[0] =='A':
                A.append(j[1])
            elif j[0] == 'B':
                B.append(j[1])
        A.sort()
        B.sort()
        print(A,B,pnum)
        tar = -1
        num=0
        stri=[]
        for l in A:
            if len(stri)<4:
                stri.append(l)
            else:
                if stri[0]+ex[0][2]<=l:
                    stri.append(l)
                    stri.pop(0)
                else:
                    stri.append(stri[0]+ex[0][2])
                    stri.pop(0)
            # print('A',stri[-1],ex[0][2])
        
        if len(stri) != 0:
            temp = stri[-1]+ex[0][2]
            print('temp',temp)
        stri = []
        for l in B:
            if len(stri) < 4:
                stri.append(l)
            else:
                if stri[0]+ex[0][2] <= l:
                    stri.append(l)
                    stri.pop(0)
                else:
                    stri.append(stri[0]+ex[1][2])
                    stri.pop(0)
            # print('B',stri[-1],ex[1][2])
        if len(stri) != 0:
            res = max(temp, stri[-1]+ex[1][2])
            print('res',res)
            ans.append(res)
        else:
            ans.append(temp)
        #  or len(B) !=0:
            
        #     time+=1

        
    print(ans)
