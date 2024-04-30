from collections import deque
m,n=map(int,input().split())
map=[list(map(int,input().split())) for _ in range(n)]
visited=[[0]*m for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
q=deque()

#익은 토마토 q에 먼저 다 넣기
for i in range(n):
    for j in range(m):
        if map[i][j]==1:
            q.append((i,j))
while q:
    x,y=q.popleft()
    visited[x][y]=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=m or visited[nx][ny]:
            continue
        if map[nx][ny]==0:
            #현재 익은 토마토 기준, 4방향 토마토 익히기, +1 (day)
            map[nx][ny]=map[x][y]+1 
            visited[nx][ny]=1
            q.append((nx,ny))

#가장 마지막에 익은 토마토 찾아주기    
result=0
for row in map:
    for j in range(len(row)):
        if row[j] == 0:
            print(-1)
            exit()
    max_row=max(row)
    result=max(result,max_row)
print(result-1)



