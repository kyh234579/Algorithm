from collections import deque
m,n=map(int,input().split(' '))
board=[list(map(int,input())) for _ in range(n)]
visited=[[-1]*m for _ in range(n)]
q=deque()
q.append([0,0])
visited[0][0]=0
dx=[-1,1,0,0]
dy=[0,0,-1,1]

while q:
    x,y=q.popleft()
    if x==n-1 and y==m-1:
        print(visited[x][y])
        break
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=m or visited[nx][ny]!=-1:
            continue
        if board[nx][ny]==0:
            visited[nx][ny]=visited[x][y]
            #빈방이면 벽보다 우선순위를 먼저 둔다.-> appendleft
            q.appendleft([nx,ny])   
        if board[nx][ny]==1:
            visited[nx][ny]=visited[x][y]+1
            q.append([nx,ny])
