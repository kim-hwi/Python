def solution(info, query):
    answer = []
    for i in query:
        temp = i.split(' ')
        count = 0
        for j in info:
            temp2 = j.split(' ')
            if (temp[0] == temp2[0] or temp[0] == '-') and (temp[2] == temp2[1] or temp[2] == '-') and (temp[4] == temp2[2] or temp[4] == '-') and (temp[6] == temp2[3] or temp[6] == '-') and (int(temp[7]) <= int(temp2[4]) or temp[7] == '-'):

                count += 1
        answer.append(count)
    print(answer)

    return answer
