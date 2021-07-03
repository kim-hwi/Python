def self (num):
    temp = str(num)
    sum = num
    for i in temp:
        sum += int(i)
    if sum<10000:
        arr.add(sum)
        return self(sum)
arr = set()
for i in range(1,10000):
    self(i)
arr2 = [i for i in range(1, 10000)]
for i in arr:
    arr2.remove(i)
for i in range(len(arr2)):
    print(arr2[i])