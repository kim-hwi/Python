mxnum=21
def dfs (now,arr,vi,depth):
    global mxnum
    if False not in vi:
        
        mxnum=min(mxnum,depth)
        return depth
    if depth == len(arr)-1:
        mxnum=min(mxnum,depth)
        return depth
    if vi[now+1]==False:
        vi[now+1]=True
        dfs(now+1,arr,vi,depth+1)
        vi[now+1]=False
    else:
        dfs(now+1,arr,vi,depth+1)
    if vi[now-1]==False:
        vi[now-1]=True
        dfs(now-1,arr,vi,depth+1)
        vi[now-1]=False
    else:
        dfs(now-1,arr,vi,depth+1)
    
    

dic={}
for i in range(13):
    dic[chr(ord('A')+i)]=i
for i in range(13):
    dic[chr(ord('N')+i)]=13-i
def solution(name):
    global mxnum
    name = list(name)
    vis=[False for i in range(len(name))]
    res=[]
    for n in name:
        res.append(dic[n])
    for i in range(len(name)):
        if name[i] =='A':
            vis[i]=True
    
    print(res)
    start=1
    last=len(name)-1
    now=0
    vis[0]=True
    print(dfs (0,name,vis,0))
    print(mxnum)
         
    
    answer = sum(res)+mxnum
    return answer