from collections import deque
import math

def pri(n):
    n=int(n)
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
    # num = int(num1)
    # if num == 1:
    #     return False
    # if num == 2:
    #     return True
    # for i in range(2,num):
    #     if num%i == 0:
    #         return False
    # return True

T = int(input())
for t in range(T):
    n,t=input().split()
    c=0
    vis=[]
    qu=deque()
    qu.append([str(n), 0])
    flag=False
    a='abc'
    ans=[]
    while qu:
        cur = qu.popleft()
        vis.append(cur[0])
        if cur[0] == str(t):
            ans.append(cur[1])
            flag = True
        else:
        # print(cur,vis)
            for i in range(4):
                for j in range(0,10):
                    
                    if i==0 and j==0:
                        continue
                    

                    # print(cur,cur[0][i],str(j),vis)
                    if cur[0][i] !=str(j):
                        temp=cur[0][0:i]+str(j)+cur[0][i+1:]
                        temp = temp.replace(" ", "")
                        if pri(temp) and temp not in vis:
                            qu.append([temp,cur[1]+1])
                            # print(temp,cur[1])
                            # vis.append(temp)
            
        
        if flag==True:
            break
    if len(ans)==0:
        print('Impossible')
    else:
        print(min(ans))


            
    # print(pri(n))
