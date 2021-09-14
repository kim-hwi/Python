st = str(input())
arr=[]
for s in st:
    arr.append(s)
    if len(arr) > 1:
        if arr[-1] == ')' and arr[-2]=='(':
            arr.pop()
            arr.pop()
            arr.append(2)
        elif arr[-1] == ']' and arr[-2]=='[':
            arr.pop()
            arr.pop()
            arr.append(3)
        elif arr[-1] == ')' and type(arr[-2])==int:
            arr.pop()
            temp = 0
            while type(arr[-1]) == int and len(arr) > 1:
                temp += arr[-1]
                arr.pop()
            arr.pop()
            arr.append(temp*2)
        elif arr[-1] == ']' and type(arr[-2]) == int:
            arr.pop()
            temp = 0
            while type(arr[-1]) == int and len(arr)>1:
                temp += arr[-1]
                arr.pop()
            
            arr.pop()
            arr.append(temp*3)
if '(' in arr or ')' in arr or '[' in arr or ']' in arr:
    print(0)

else:
    print(sum(arr))
