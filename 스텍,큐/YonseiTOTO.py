n,mail= input().split()
res=[]
for i in range(int(n)):
    pe,lim=input().split()
    pe=int(pe)
    lim=int(lim)
    arr=list(map(int,input().split(' ')))
    if pe<lim:
        res.append(1)
    else:
        arr.sort(reverse=True)
        res.append(arr[lim-1])
# print(sorted(res))
ans=0
count=0
for i in sorted(res):
    if ans+i <= int(mail):
        ans+=i
        count+=1
print(count)

