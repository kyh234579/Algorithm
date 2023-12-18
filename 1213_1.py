def primeNumber(x):
    for i in range(2,x):
        if x % i == 0:
           return False
    return True
m=int(input())
n=int(input())

arr=[]
for k in range(m,n+1):
    if k ==1:
        continue
    if primeNumber(k):
        arr.append(k)
if arr == []:
    print(-1)
else: 
    print(sum(arr))
    print(min(arr))