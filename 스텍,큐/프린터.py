def solution(pri, loc):
    arr = [i for i in range(len(pri))]
    count = 0
    answer = 0
    while(len(pri) != 0):
        flag = True
        for i in range(1, len(pri)):
            if pri[0] < pri[i]:
                pri.append(pri.pop(0))
                arr.append(arr.pop(0))
                flag = False
                break
        if flag == True:
            count += 1
            pri.pop(0)
            if loc == arr.pop(0):
                answer = count

    return answer
