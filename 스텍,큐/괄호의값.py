st = str(input())
arr=[]
for s in st:
    if s == ')':
        if len(arr)>0:
            if arr[-1]=='(':
                arr.pop()
                arr.append(2)
            elif type(arr[-1]) == int:
                temp=0
                while len(arr) > 0 and type(arr[-1]) == int:
                    temp += arr[-1]
                    arr.pop()
                if len(arr) == 0:
                    print(0)
                    exit(0)
                if arr[-1] != '(':
                    print(0)
                    exit(0)
                arr.pop()
                arr.append(temp*2)
            else:
                print(0)
                exit(0)
        else:
            print(0)
            exit(0)


    elif s == ']':
        if len(arr) > 0:
            if arr[-1] == '[':
                arr.pop()
                arr.append(3)
            elif type(arr[-1]) == int:
                temp = 0

                while len(arr)>0 and type(arr[-1]) == int:
                    temp += arr[-1]
                    arr.pop()
                if len(arr) == 0:
                    print(0)
                    exit(0)
                if arr[-1] != '[':
                    print(0)
                    exit(0)
                arr.pop()
                arr.append(temp*3)
            else:
                print(0)
                exit(0)
        else:
            print(0)
            exit(0)
    else:
        arr.append(s)

        # elif arr[-1] == ']' and arr[-2]=='[':
        #     arr.pop()
        #     arr.pop()
        #     arr.append(3)
        # elif arr[-1] == ')' and type(arr[-2])==int:
        #     arr.pop()
        #     temp = 0
        #     while type(arr[-1]) == int and len(arr) > 1:
        #         temp += arr[-1]
        #         arr.pop()
        #     arr.pop()
        #     arr.append(temp*2)
        # elif arr[-1] == ']' and type(arr[-2]) == int:
        #     arr.pop()
        #     temp = 0
        #     while type(arr[-1]) == int and len(arr)>1:
        #         temp += arr[-1]
        #         arr.pop()
            
        #     arr.pop()
        #     arr.append(temp*3)
# print(arr)
if '(' in arr or ')' in arr or '[' in arr or ']' in arr:
    print(0)

else:
    print(sum(arr))
