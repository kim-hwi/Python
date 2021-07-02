testcase = int(input())
arr = [input() for i in range(testcase)]
score = 0
temp = 1
for i in range(testcase):
    for j in arr[i]:
        if j == "O":
            score +=temp
            temp+=1
        elif j == "X":
            temp = 1
    print(score)
    score = 0
    temp = 1 
    
