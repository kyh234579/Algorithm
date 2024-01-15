from collections import deque
n,l,r=map(int,input().split())
people=[list(map(int,input().split())) for _ in range(n)]
queue=deque()
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(x,y):
    queue.append((x,y))
    union=[]
    union.append((x,y))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n or visited[nx][ny]:
                continue
            if l<=abs(people[x][y]-people[nx][ny])<=r:
                visited[nx][ny]=True
                queue.append((nx,ny))
                union.append((nx,ny))
    if len(union) <= 1:
        return 0
    result= sum(people[a][b] for a,b in union) // len(union)
    for a,b in union:
        people[a][b]=result
    return 1
day=0
while True:
    flag=0
    visited=[[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j]=True
                flag+=bfs(i,j)
    if flag==0:
        break
    day+=1
print(day)