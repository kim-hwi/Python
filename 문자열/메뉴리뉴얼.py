def solution(orders, course):
    intersection = []
    answer = []
    orders.sort(key=len)
    print(orders)
    for i in range(len(orders)):
        for j in range(i+1, len(orders)):
            intersection.append(list(set(orders[i]) & set(orders[j])))
    for j in course:
        for i in intersection:
            i.sort()
            if len(i) == j:
                temp = ''
                for k in range(len(i)):
                    temp += str(str(i[k]))
                answer.append(temp)
                print(answer)
    answer = list(set(answer))
    answer.sort(key=len)
    temp = []
    for i in answer:
        temp = []
        count = 0
        for k in orders:
            if list(set(i) & set(k)) != []:
                count += 1
        temp.append([i, count])

    print('temp', temp)

    return answer
