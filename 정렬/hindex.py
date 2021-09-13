def solution(citations):
    maxnum = 0
    for i in range(len(citations)+1):
        count = 0
        for non in citations:
            # print(non)
            if i <= int(non):
                count += 1
        if count >= i:
            maxnum = max(i, maxnum)
    answer = maxnum
    return answer
