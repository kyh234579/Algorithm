import sys
input=sys.stdin.readline
n=int(input())
arr=[]
for _ in range(n):
    d,t=map(int,input().split())
    arr.append([d,t])
arr.sort(key=lambda x:x[1],reverse=True)
now=float('inf')
for d,t in arr:
    now=min(now,t)-d
if now<=0:
    print(0)
else:
    print(now)