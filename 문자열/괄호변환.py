
test = str(input())


def solution(p):
    answer = ''
    u=''
    v=''
    if p == '':
        return answer
    leftnum = 0
    rightnum = 0
    flag = False
    recursive = False
    for i in p:
        if i == '(':
            if flag == False:
                leftnum += 1
                u += i
            if flag == True:
                v += i
        if i == ')':
            if flag == False:
                rightnum += 1
                u += i
            if flag == True:
                v += i
        if leftnum==rightnum and flag == False:
            flag = True
            resnum = 0
            for j in u:
                if j == '(':
                    resnum += 1
                if j == ')':
                    resnum -= 1
                if resnum == -1:
                    recursive = True

    if recursive == True:
        u = u[1:len(u)-1]
        temp = ''
        for k in u:
            if k == '(':
                temp+=')'
            else:
                temp+='('    
        u = temp
        return '('+solution(v)+')'+u

    if resnum != 0:
        u = u[1:len(u)-1]
        temp = ''
        for k in u:
            if k == '(':
                temp += ')'
            else:
                temp += '('
        u = temp
        return '('+solution(v)+')'+u

    return u+solution(v)
    


print(solution(test))
# print(test[len(test)-1])
