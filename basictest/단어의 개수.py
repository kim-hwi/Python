st = str(input())
count = 1
if st[0] ==' ':
    count-=1
if st[len(st)-1] ==' ':
    count -= 1
for i in st:
    if i == ' ':
        count+=1
print(count)
