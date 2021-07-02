testcase = int(input())
max = 0
res = 0
score = list(map(int,input().split(' ')))
for i in range(testcase):
    if score[i] > max:
        max = score[i]
for i in range(testcase):
    score[i] = score[i]/max*100
    res += score[i]
print(res/testcase)

