from collections import deque
T = int(input())
for t in range(T):
    N,tar=map(int,input().split())
    arr=deque()
    num=0
    for i in input().split():
        arr.append([i,num])
        num+=1
    cout=0
    while len(arr) != 0:
        flag=False
        temp = arr.popleft()
        for i in range(len(arr)):
            if temp[0]<arr[i][0]:
                arr.append(temp)
                flag=True
                break
        
        if flag == True:
            continue
        cout+=1
        if temp[1] == tar:
            print(cout)
            break
                

    
    
    
