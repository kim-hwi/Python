snum = int(input())
for i in range(0, snum):
    for j in range(0, snum):
        if snum-i-1>j:
            print(" ",end='')
        else: 
            print("*", end='')
    print()
