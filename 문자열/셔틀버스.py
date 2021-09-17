def solution(n, t, m, timetable):
    arrpep = []

    arrbus = []
    last = 540+(n-1)*t
    for i in timetable:
        temp = int(i[0:2])*60+int(i[3:5])
        if temp <= last:
            arrpep.append(temp)
    arrpep.sort()

    for i in range(n):
        arrbus.append(540+(i)*t)

    for i in range(len(arrbus)-1):
        pep = 0
        for j in arrpep:
            if j <= arrbus[i]:
                pep += 1
                arrpep.pop(0)
            if pep >= m:
                break

    if len(arrpep) >= m:
        answertemp = arrpep[m-1]-1
    else:
        answertemp = last

#     print(answertemp)

#     print(arrpep)
#     print(arrbus)

    temp1 = int(answertemp/60)
    if temp1 < 10:
        temp1 = '0'+str(temp1)
    else:
        temp1 = str(temp1)

    temp2 = int(answertemp % 60)
    if temp2 < 10:
        temp2 = '0'+str(temp2)
    else:
        temp2 = str(temp2)

    return temp1+':'+temp2
