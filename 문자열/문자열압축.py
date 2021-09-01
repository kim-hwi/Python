from typing import Sized
import math

s = str(input())
def sol(s):
    arr=[]
    res = len(s)
    for n in range(1,math.ceil(len(s)/2)+1):
        for i in range(0, len(s), n):
            arr.append(s[i:i + n])
        temp = 0
        restemp = len(s)
        next = 1
        print(arr)
        flag = False
        for i in arr:
            if(i == temp and flag == True):
                restemp -= n
                next += 1
                print("true",i,next, restemp)
                
                if next==10 or next ==100 or next ==1000:
                    restemp+=1
            elif(i==temp and flag == False):
                restemp-=n
                restemp+=1
                next+=1
                print("false", i, next, restemp)
                flag = True
                
            else:
                temp = i
                flag = False
        res = min(res,restemp)
        arr.clear()
    print(res)
                  
sol(s)

