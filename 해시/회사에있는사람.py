N = int(input())
dic=dict()
for i in range(N):
    name,inout=input().split(' ')
    # print(name,inout)
    if inout == 'enter':
        dic[name]=1
    else:
        if dic[name]:
          del dic[name]
        
ans = sorted(dic,reverse=True)
for i in ans:
    print(i)
