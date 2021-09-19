T = int(input())




# def dfs(x, y, dir,arr, end):
#     if dir[0] == 0:
#         dir0 = dir.copy()
#         dir1 = dir.copy()
#         dir0[1]+=1
#         dir1[1]+=1
#         dir1[0]=1
#         nx=x+dix[0]
#         ny=y+diy[0]
#         if nx<0 or ny<0 or nx>=n or ny>=n:
#             return
#         if board[nx][ny] in arr:
#             return
#         arr0=arr.copy()
#         arr0.append(board[nx][ny])
#         dfs(nx, ny, dir0, arr0, end)
#         dfs(nx, ny, dir1, arr0, end)
    
#     if dir[0] == 1:
#         dir0 = dir.copy()
#         dir1 = dir.copy()
#         dir0[2] = +1
#         dir1[2] = +1
#         dir1[0] = 2
#         nx = x+dix[1]
#         ny = y+diy[1]
#         if nx < 0 or ny < 0 or nx >= n or ny >= n:
#             return
#         if board[nx][ny] in arr:
#             return
#         arr0 = arr.copy()
#         arr0.append(board[nx][ny])
#         dfs(nx, ny, dir0, arr0, end)
#         dfs(nx, ny, dir1, arr0, end)
#     if dir[0] == 2:
#         dir0 = dir.copy()
#         dir1 = dir.copy()
#         dir0[3] = +1
#         dir1[3] = +1
#         dir1[0] = 3
#         nx = x+dix[1]
#         ny = y+diy[1]
#         if nx < 0 or ny < 0 or nx >= n or ny >= n:
#             return
#         if board[nx][ny] in arr:
#             return
#         arr0 = arr.copy()
#         arr0.append(board[nx][ny])
#         dfs(nx, ny, dir0, arr0, end)
#         if dir1[1] == dir0[3]:
#             dfs(nx, ny, dir1, arr0, end)


dix = [-1, 1, 1, -1]
diy = [1, 1, -1, -1]

def fun (x,y):
    
    for l in range(2, n):
        for k in range(2, n):
            if l+k >= n+2:
                continue
            arr = [board[x][y]]
            curx = x
            cury = y
            
            flag = False
            for i in range(k):
                curx -=1
                cury +=1
                # print(l, k, curx, cury)
                if curx<0 or cury<0 or curx>=n or cury>=n:
                    flag = True
                    break
                if board[curx][cury] in arr:
                    flag = True
                    break
                arr.append(board[curx][cury])
            if flag == True:
                flag = False
                break
            
            for i in range(l):
                curx += 1
                cury += 1
                if curx < 0 or cury < 0 or curx >= n or cury >= n:
                    flag = True
                    break
                if board[curx][cury] in arr:
                    flag = True
                    break
                arr.append(board[curx][cury])
            if flag == True:
                flag = False
                break

            for i in range(k):
                curx += 1
                cury -= 1
                if curx < 0 or cury < 0 or curx >= n or cury >= n:
                    flag = True
                    break
                if board[curx][cury] in arr:
                    flag = True
                    break
                arr.append(board[curx][cury])
            if flag == True:
                flag = False
                break
            
            for i in range(l-1):
                curx -= 1
                cury -= 1
                if curx < 0 or cury < 0 or curx >= n or cury >= n:
                    flag = True
                    break
                if board[curx][cury] in arr:
                    flag = True
                    break
                arr.append(board[curx][cury])
            if flag == True:
                flag = False
                break
        #     for i in range(k):
        #         curx += 1
        #         cury += 1
        #         arr.append(board[curx][cury])
        #     for i in range(k):
        #         curx += 1
        #         cury -= 1
        #         arr.append(board[curx][cury])
        #     for i in range(k):
        #         curx -= 1
        #         cury -= 1
        #         arr.append(board[curx][cury])
            # if len(arr) == 12:
            print(x,y,arr,len(arr))


            arrsum.append(len(arr))
            

for t in range(1,T+1):
    global n
    n = int(input())
    global board
    global arrsum
    arrsum=[]
    board = [[int(i) for i in input().split(' ')]for j in range(n)]
    # board = [[int(i) for i in range(10)]for j in range(n)]
    
    
    for i in range(n):
        print(board[i])
    for i in range(n):
        for j in range(n):
            fun(i, j)
    # fun(2,2)
    # print(board[2][2])
    if len(arrsum) == 0:
        print('#', t, ' ', -1, sep='')
    else:
        print('#',t,' ',max(arrsum),sep='')
    print(arrsum)        
            # dfs(i,j,[0,0,0,0,0],[board[i][j]],[i,j])
