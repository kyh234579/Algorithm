from collections import deque
n,k=map(int,input().split())
max=100001
visited=[-1]*max
q=deque()
q.append(n)
visited[n]=0

while q:
    x=q.popleft()
    if x == k:
        print(visited[x])
        break
    #우선순위 *2-> -1 -> +1
    if 0<=x*2<max and visited[x*2]==-1:
        #가장 우선순위, 앞으로 집어넣기
        q.appendleft(x*2)
        visited[x*2]=visited[x]
    if 0<=x-1<max and visited[x-1]==-1:
        q.append(x-1)
        visited[x-1]=visited[x]+1
    if 0<=x+1<max and visited[x+1]==-1:
        q.append(x+1)
        visited[x+1]=visited[x]+1
      
    
