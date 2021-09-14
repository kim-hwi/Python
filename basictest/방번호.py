import math
num = str(input())

number = [0 for i in range(10)]

for i in num:
    number[int(i)]+=1
temp = number[9]+number[6]
temp = math.ceil(temp/2)
number[9] = temp
number[6] = temp

print(number)
print(max(number))