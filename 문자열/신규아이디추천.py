id = str(input())


def solution(id):
    num = 1
    newid = ''
    for i in id:
        if(len(newid) == 15):
            break
        elif ord(i) < 90 and ord(i) > 64:
            i = chr(ord(i)+32)
            newid += i
        elif ((ord(i) >= 48 and ord(i) <= 57) or (ord(i) >= 97 and ord(i) <= 122) or ord(i) == 45 or ord(i) == 95 or ord(i) == 46):
            if(ord(i) == 46 and len(newid) > 0):
                if newid[-1] == '.':
                    continue
                elif newid[0] == '.':
                    continue
                else:
                    newid += i
            elif(ord(i) == 46 and len(newid) == 0):
                continue
            else:
                newid += i
        num += 1

    if len(newid) == 0:
        newid = 'aaa'
    if newid[-1] == '.':
        newid = newid[0:len(newid)-1]
    if len(newid) < 3:
        while(len(newid) < 3):
            newid += newid[-1]

    answer = newid
    print(answer)
    return answer
    
print(solution(id))
