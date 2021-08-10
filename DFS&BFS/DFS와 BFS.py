com, line, start = map(int,input().split())
arr=[]
for i in range(line):
    arr.append(list(map(int,input().split())))
arr.sort()
temp =[]
buf = [start]
vist = [False for i in range(com+1)]
vist[start] = True
print(start, end=' ')
while len(buf) != 0:
    nowstart = buf.pop()
    if vist[nowstart] == False:
        print(nowstart, end=' ')
    vist[nowstart] = True

    for i in range(line):
        if arr[i][0] == nowstart and vist[arr[i][1]] == False:
            temp.append(arr[i][1])
        elif arr[i][1] == nowstart and vist[arr[i][0]] == False:
            temp.append(arr[i][0])
    temp.sort()
    # print(temp)
    # print(buf)
    while len(temp) != 0:
        buf.append(temp.pop())
print()


vist = [False for i in range(com+1)]
# print(vist,temp,buf)
buf = [start]

vist[start] = True
    
while len(buf) != 0:
    nowstart = buf.pop(0)
    print(nowstart, end=' ')
    for i in range(line):
        if arr[i][0] == nowstart and vist[arr[i][1]] == False:
            temp.append(arr[i][1])
            vist[arr[i][1]] = True
        elif arr[i][1] == nowstart and vist[arr[i][0]] == False:
            temp.append(arr[i][0])
            vist[arr[i][0]] = True
    temp.sort()
    while len(temp) != 0:
        buf.append(temp.pop(0))
