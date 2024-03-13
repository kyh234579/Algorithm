n=int(input())
arr=[]
for _ in range(n):
    #소요시간, 마감시간
    t,s=map(int,input().split())
    arr.append([t,s])
arr.sort(key=lambda x:x[1],reverse=True)
now=float('inf')
for t,s in arr:
    now=min(now,s)-t
if now<0:
    print(-1)
else:
    print(now)
