com, line, start = map(int,input().split())
arr=[]
dic = {i:[] for i in range(com+1)}

for i in range(line):
    arr.append(list(map(int,input().split())))
    a = min(arr[-1])
    b = max(arr[-1])
    dic[a].append(b)
    dic[b].append(a)

arr.sort()
for i in range(com+1):
    dic[i].sort()
# print(dic)

vist = [False for i in range(com+1)]
vist[start] = True
buf = [start]


def dfs (v):
    global vist
    print(v,end=' ')
    for i in range(len(dic[v])):
        # print(dic[v][i])
        if vist[dic[v][i]] == False:
            vist[dic[v][i]] = True
            dfs(dic[v][i])
dfs(start)
print()

# vist=[False for i in range(com+1)]
# buf=[start]
# vist[start] = True
# print(start, end=' ')
# while buf:
#     temp=[]
#     nowstart = buf.pop()
    
#     if vist[nowstart] == False:
#         print(nowstart, end=' ')
#     vist[nowstart] = True
#     for i in range(line):
#         if nowstart == arr[i][0] and vist[ arr[i][1] ] == False:
#             temp.append(arr[i][1])
#         if nowstart == arr[i][1] and vist[arr[i][0]] == False:
#             temp.append(arr[i][0])
#     temp.sort()
#     while len(temp) != 0:
#         buf.append(temp.pop())
# print()


















# temp =[]
# buf = [start]

# vist = [False for i in range(com+1)]
# vist[start] = True

# print(start, end=' ')
# while len(buf) != 0:
#     nowstart = buf.pop()
#     if vist[nowstart] == False:
#         print(nowstart, end=' ')
#     vist[nowstart] = True

#     for i in range(line):
#         if arr[i][0] == nowstart and vist[arr[i][1]] == False:
#             temp.append(arr[i][1])
#         elif arr[i][1] == nowstart and vist[arr[i][0]] == False:
#             temp.append(arr[i][0])
#     temp.sort()
#     while len(temp) != 0:
#         buf.append(temp.pop())
# print()




# vist = [False for i in range(com+1)]
# # print(vist,temp,buf)
# buf = [start]

# vist[start] = True
    
# while len(buf) != 0:
#     nowstart = buf.pop(0)
#     print(nowstart, end=' ')
#     for i in range(line):
#         if arr[i][0] == nowstart and vist[arr[i][1]] == False:
#             temp.append(arr[i][1])
#             vist[arr[i][1]] = True
#         elif arr[i][1] == nowstart and vist[arr[i][0]] == False:
#             temp.append(arr[i][0])
#             vist[arr[i][0]] = True
#     temp.sort()
#     while len(temp) != 0:
#         buf.append(temp.pop(0))





vist = [0 for i in range(com+1)]
buf=[start]
vist[start] = 1
while buf:
    temp=[]
    nowstart = buf.pop(0)
    print(nowstart,end=' ')
    for i in range(line):
        if nowstart == arr[i][0] and vist[ arr[i][1] ] ==0:
            temp.append(arr[i][1])
            vist[arr[i][1]] = 1
        if nowstart == arr[i][1] and vist[arr[i][0]] == 0:
            temp.append(arr[i][0])
            vist[arr[i][0]] = 1
    temp.sort()
    while temp:
        buf.append(temp.pop(0))



