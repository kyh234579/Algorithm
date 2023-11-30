n=int(input())
arr=[]
for i in range(n):
    a,b=map(int,input().split())
    arr.append((a,b))

arr.sort(reverse=True)
max=0
cnt=0
for a,b in arr:
    if b > max:
        max=b
        cnt+=1
print(cnt)