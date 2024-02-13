from collections import deque
a,b=map(int,input().split())
q=deque()
q.append((a,1))
result=[]

while q:
    x,cnt=q.popleft()
    if x==b:
        result.append(cnt)
        break
    if x*2<=b :
        q.append((x*2,cnt+1))
    if int(str(x)+str(1))<=b:
        q.append((int(str(x)+str(1)),cnt+1))

if len(result)==0:
    print(-1)
else:
    print(result[-1])
