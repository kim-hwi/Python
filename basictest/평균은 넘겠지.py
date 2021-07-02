testcase = int(input())
res = []
for i in range(testcase):
    avg = 0
    cont = 0
    arr = list(map(int,input().split()))
    for j in range(1,arr[0]+1):
        avg += arr[j]
    avg = avg/arr[0]
   
    for j in range(1, arr[0]+1):
        if arr[j]>avg:
            cont+=1
    res.append(cont/arr[0])
for i in range(testcase):
    print("{:.3f}%".format(res[i]*100)) 
