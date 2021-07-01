import time
num = int(input())
res = num

count = 0
while True:
    # time.sleep(0.5)
    num1 = num//10
    num2 = num%10
    num3 = (num1+num2)%10
    num4 = num3 + num2*10
    count += 1
    # print(num1, num2, num3, num4)
    if num4 == res:
        break
    num = num4

print(count)

