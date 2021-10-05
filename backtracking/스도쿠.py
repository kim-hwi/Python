

board = [[int(i) for i in input().split()]for j in range(9)]



def bun(x,y):
    ans = []
    temp = [[0,3,0,3],[0,3,3,6],[0,3,6,9],[3,6,0,3],[3,6,3,6],[3,6,6,9],[6,9,0,3],[6,9,3,6],[6,9,6,9]]
    for t in temp:
        # print(type(t[0]),type(x))
        if x>=t[0] and x<t[1] and y>=t[2] and y<t[3]:
            for i in range(9):
                for j in range(9):
                    if t[0]<=i and i<t[1] and t[2]<=j and j<t[3]:
                        ans.append([i,j])
            return ans 

def dfs(depth,x,y,n):
    global vis
    # print(vis,x,y)
    for i in range(1,10):
        a = [board[l[0]][l[1]] for l in bun(x, y)].count(i)
        b = [board[l][y] for l in range(9)].count(i)
        c = board[x].count(i)
        if a>1 or b>1 or c>1:
            return
    
    if depth == 10:
        for i in range(9):
            for j in range(9):
                # print(i,j)
                print( board[i][j] , end=' ')
            print()
        print('/')
        exit(0)

    for i in range(len(vis)):
        for j in range(len(vis[i][1])):
            board[vis[i][0][0]][vis[i][0][1]] = vis[i][1][j]
            print(vis[i], i, depth, x, y, n, vis[i][1][j])
            print(vis[i][0][0], vis[i][0][1],)
            dfs(depth+1, vis[i][0][0], vis[i][0][1], n)
            board[vis[i][0][0]][vis[i][0][1]] = 0
        


num=set([1,2,3,4,5,6,7,8,9])
vis=[]
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            temp=[]
            w = num-set(board[i])
            r = num-set([board[l][j] for l in range(9)])
            b = num -set([board[l[0]][l[1]] for l in bun(i,j)])
            temp = w&r&b
            # print(temp)
            if len(temp) == 1:
                temp=list(temp)
                board[i][j] = temp[0]
            else:
                vis.append([[i,j],list(temp)])
print()
if len(vis)==0:
    for i in range(9):
        for j in range(9):
            print(board[i][j],end=' ')
        print()
    
else:
    print()
    dfs(0, vis[0][0][0], vis[0][0][1], len(vis))



