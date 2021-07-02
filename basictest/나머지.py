cont = [0 for i in range(42)]
count = 0
for i in range(10):
    num = int(input())
    cont[num%42] = 1

for i in range(42):
    if cont[i] != 0:
        count+=1
print(count)
