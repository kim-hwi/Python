def solution(record):
    dic = {}
    answer = []
    for i in record:
        arr = i.split(' ')
        if arr[0] == 'Enter':
            dic[arr[1]] = arr[2]
            answer.append()
        if arr[0] == 'Change':
            dic.update({arr[1]: arr[2]})
        print(dic)
    

    return answer
