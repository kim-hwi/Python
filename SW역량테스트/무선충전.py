T = int(input())

dix = [0,-1,0,1,0]
diy = [0,0,1,0,-1]

for t in range(T):
    M,A = map(int,input().split())
    usA = [int(i) for i in input().split()]
    usB = [int(i) for i in input().split()]
    ap=[]
    for i in range(A):
        temp = list(map(int,input().split(' ')))
        ap.append(temp)
    
    # print(usA,usB)
    # for i in ap:
        # print(i)

    Asum=0
    Bsum=0

    vis=[[[] for i in range(10)] for j in range(10)]
    
    curAx = 0
    curAy = 0
    curBx = 9
    curBy = 9
    count = 0
    
    chA = []
    chB = []
    for ch in ap:
        if abs(ch[0]-1-curAy)+abs(ch[1]-1-curAx) <= ch[2]:
                chA.append([ch[3], ap.index(ch)])
        if abs(ch[0]-1-curBy)+abs(ch[1]-1-curBx) <= ch[2]:
                chB.append([ch[3], ap.index(ch)])
        chA.sort(reverse=True)
        chB.sort(reverse=True)

    # print(chB)

    if len(chA) == 1 and len(chB) == 1 and chA[0][1] == chB[0][1]:
        Asum += int(chA[0][0]/2)
        Bsum += int(chB[0][0]/2)
    elif len(chA) == 1 and len(chB) > 1 and chA[0][1] == chB[0][1]:
        Asum += chA[0][0]
        Bsum += chB[1][0]
    elif len(chB) == 1 and len(chA) > 1 and chA[0][1] == chB[0][1]:
        Bsum += chB[0][0]
        Asum += chA[1][0]
    else:
        if len(chA)>0:
            Asum += chA[0][0]
        if len(chB) > 0:
            Bsum += chB[0][0]


    for i in range(len(usA)):
        for dir in range(5):
            if dir == usA[i]:
                curAx = curAx+dix[dir]
                curAy = curAy+diy[dir]
            if dir == usB[i]:    
                curBx = curBx+dix[dir]
                curBy = curBy+diy[dir]
                # print(dir,curBx,curBy)
        chA=[]
        chB=[]


        for ch in ap:
            if abs(ch[0]-1-curAy)+abs(ch[1]-1-curAx)<=ch[2]:
                chA.append([ch[3], ap.index(ch)])
            if abs(ch[0]-1-curBy)+abs(ch[1]-1-curBx) <= ch[2]:
                chB.append([ch[3], ap.index(ch)])


        
        chA.sort(reverse=True)
        chB.sort(reverse=True)

        # print(chB)

        if len(chA) == 1 and len(chB) == 1 and chA[0][1] == chB[0][1]:
            Asum += int(chA[0][0]/2)
            Bsum += int(chB[0][0]/2)
        elif len(chA) == 1 and len(chB) > 1 and chA[0][1] == chB[0][1]:
            Asum += chA[0][0]
            Bsum += chB[1][0]
        elif len(chB) == 1 and len(chA) > 1 and chA[0][1] == chB[0][1]:
            Bsum += chB[0][0]
            Asum += chA[1][0]
        elif len(chB) > 1 and len(chA) > 1 and chA[0][1] == chB[0][1]:
            Bsum += chB[0][0]
            Asum += max(chA[1][0],chB[1][0])
        else:
            if len(chA)>0:
                Asum += chA[0][0]
            if len(chB) > 0:
                Bsum += chB[0][0]


     
        # elif len(charr) > 1:
        #     charr.sort(reverse=True)
        #     vis[curx][cury] = charr[0]
        # Asum += charr[0][0]
    print ('#',t+1,' ',Asum+Bsum,sep='')



