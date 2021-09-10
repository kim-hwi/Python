def ROT(num, whe):
    if num == 3:
        if whe == 1:
            
            if mag[num][6] != mag[num-1][2] and vis[num-1] == 0:
                vis[num] = 1
                ROT(num-1, -1)
            vis[num] = 1
            temp = mag[num]
            temparr[num].insert(0, temp.pop())
        
        else:
            if mag[num][6] != mag[num-1][2] and vis[num-1] == 0:
                vis[num] = 1
                ROT(num-1, 1)
            vis[num] = 1
            temp = mag[num]
            temparr[num].append(temp.pop(0))
        return
    
    if num == 0:
        if whe == 1:
            
            if mag[num][2] != mag[num+1][6] and vis[num+1] == 0:
                vis[num] = 1
                ROT(num+1, -1)
            vis[num] = 1
            temp = mag[num]
            temparr[num].insert(0, temp.pop())
        
        else:
            if mag[num][2] != mag[num+1][6] and vis[num+1] == 0:
                vis[num] = 1
                ROT(num+1, 1)
            vis[num] = 1
            temp = mag[num]
            temparr[num].append(temp.pop(0))
        return
    
    if whe == 1:
        if mag[num][2] != mag[num+1][6] and vis[num+1] == 0:
            vis[num] = 1
            ROT(num+1, -1)
        if mag[num][6] != mag[num-1][2] and vis[num-1] == 0:
            vis[num] = 1
            
            ROT(num-1, -1)
        vis[num] = 1
        temp = mag[num]
        temparr[num].insert(0, temp.pop())
    
    else:
        if mag[num][2] != mag[num+1][6] and vis[num+1] == 0:
            vis[num] = 1
            ROT(num+1, 1)
        if mag[num][6] != mag[num-1][2] and vis[num-1] == 0:
            vis[num] = 1
            ROT(num-1, 1)
        vis[num] = 1
        temp = mag[num]
        temparr[num].append(temp.pop(0))
        


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    score = 0
    rotatenum = int(input())
    mag=[[i for i in input().split(' ')] for j in range(4)]
    rotate = [[i for i in input().split(' ')] for j in range(rotatenum)]
    vis=[0,0,0,0]
    temparr = mag
    for rot in rotate:
        vis = [0, 0, 0, 0]
        # print(int(rot[0])-1, int(rot[1]))
        ROT(int(rot[0])-1,int(rot[1]))
        mag = temparr
        # print(mag)
    for i in range(4):
        
        if mag[i][0] == str(1):
            score+=2**i
    # 
    print('#',test_case,' ',score,sep='')
    
