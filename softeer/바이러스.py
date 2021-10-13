import sys
k, p, n = map(int, input().split())
num = p
for i in range(n-1):
    num = ((num % 1000000007)*(p % 1000000007)) % 1000000007
print(num*k % 1000000007)
# print(k,p,n)
