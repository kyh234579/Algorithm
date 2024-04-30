from collections import deque
n,k=map(int,input().split())
sam=list(map(int,input().split()))
dic={}
queue=deque()
#dict에 key=>위치, value=>불행도로 저장.
#샘터 위치, dic에 불행도 0으로 저장.
for s in sam:
    dic[s]=0
    queue.append(s)

total=0
cnt=0    
#샘터로 시작해서 bfs 수행
while queue:
    x=queue.popleft()
    lc=x-1
    rc=x+1
    if lc not in dic.keys():
        dic[lc]=dic[x]+1
        total+=dic[lc]
        cnt+=1
        if cnt==k:
            break
        queue.append(lc)
    if rc not in dic.keys():
        dic[rc]=dic[x]+1
        total+=dic[rc]
        cnt+=1
        if cnt==k:
            break
        queue.append(rc)

print(total)
         
