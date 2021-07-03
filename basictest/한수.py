
cot = 0
def han(num):
    global cot
    arr = str(num)
    temp = 0
    if len(arr) < 3:
        cot += 1
        
        return
    else:
        temp = int(arr[0])-int(arr[1])
        
        for i in range(len(arr)-1):
            
            if int(arr[i])-int(arr[i+1]) != temp:
               return
        cot +=1


testcase = int(input())


for i in range(1,testcase+1):
    han(i)
print(cot)

