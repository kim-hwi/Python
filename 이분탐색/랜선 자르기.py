K,N = map(int,input().split())
arr = [int(input()) for i in range(K)]
last = min(arr)
first = 1
mid = 0
Fea = 1
Mea = 1
Lea = 1

arrmax = [0,0]

while(True):
    Fea,Mea,Lea = map(int,[0,0,0])
    mid = int((first+last)/2)
    for i in range(K):
        Fea += int(arr[i]/first)
    for i in range(K):
        Mea += int(arr[i]/mid)
        # print(arr[i],mid,Mea)
    for i in range(K):
        Lea += int(arr[i]/last)
    # arr[0] = max(Fea,Mea,Lea)
    print(first, mid, last, Fea, Mea, Lea)
    if Mea < N:
        last = mid
    if Mea >= N: 
        first = mid   
    
    print(first, mid, last, Fea, Mea, Lea)
    if Fea == Mea or Mea == Lea:
        break
temp = max(Fea,Mea,Lea)
if temp == Fea:
    print(first)
if temp == Mea:
    print(mid)
if temp == Lea:
    print(last)
print(int((first+last+mid)/3))
# print(int(7/2))
