def solution(record):
    dic = {}
    answer = []
    answer2 = []
    for i in record:
        arr = i.split(' ')
        if arr[0] == 'Enter':
            dic[arr[1]] = arr[2]
            answer.append([arr[1], 'in'])
        elif arr[0] == 'Change':
            dic.update({arr[1]: arr[2]})
        elif arr[0] == 'Leave':
            answer.append([arr[1], 'out'])

    for i in answer:
        if i[1] == 'in':
            answer2.append(dic[i[0]]+'님이 들어왔습니다.')

        elif i[1] == 'out':
            answer2.append(dic[i[0]]+'님이 나갔습니다.')

    return answer2
