import math
def solution(lines):
    # print(lines)
    time=[]
    timelist=[]
    for l in lines:
        l=l.split(' ')
        # print(l)
        # print(l[1][0:2],l[1][3:5],l[1][6:8])
        # print(l[2][:-1])
        s = float(l[1][0:2])*3600+float(l[1][3:5])*60+float(l[1][6:])-float(l[2][:-1])+0.001
        s=round(s,3)
        f = float(l[1][0:2])*3600+float(l[1][3:5])*60+float(l[1][6:])
        time.append([s,f])
        timelist.append(s)
        timelist.append(f)
    # print(time)
    # print()
    # print(timelist)
    res=[]
    for t in timelist:
        temp1=0
        temp2=0
        # print()
        for tim in time:
            s = tim[0]
            f = tim[1]
            mt=round(t-0.999,3)
            pt=round(t+0.999,3)
            if (mt<=f and t>=s) or (mt>=s and t<=f):
                temp1+=1
            if (t<=f and pt>=s) or (t>=s and pt<=f):
                temp2+=1
            # print(s,f,' ',mt,t,pt,' ', temp1,temp2)
        res.append(temp1)
        res.append(temp2)
    print(res)
    
    answer = 0
    return max(res)