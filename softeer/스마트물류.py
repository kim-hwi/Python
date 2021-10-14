import sys
n,k=map(int,input().split())
arr=[i for i in input()]
res=0
for i in range(len(arr)):
    if arr[i] == 'P':
        for j in range(-k,k+1):
            if i+j<0 or i+j>=n:
                continue
            if arr[i+j]=='H':
                arr[i+j]='N'
                res+=1
                break
print(res)