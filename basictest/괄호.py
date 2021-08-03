testcase = int(input())
arr=[]
temp=[0]
for i in range(testcase):
    arr.append(str(input()))
for i in range(testcase):
    for j in range(len(arr[i])):
        if temp[-1] == '(' and arr[i][j] ==')':
            temp.pop()
        else:
            temp.append(arr[i][j])
    if len(temp)==1:
        print('YES')
    else:
        print('NO')
    temp.clear()
    temp=[0]
