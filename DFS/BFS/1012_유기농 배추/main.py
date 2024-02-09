from collections import deque

T=int(input())
for _ in range(T):
    m,n,baechu=map(int,input().split())
    graph=[[0]*m for _ in range(n)]
    visited=[[0]*m for _ in range(n)]
    for _ in range(baechu):
        y,x=map(int,input().split())
        graph[x][y]=1

    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    q=deque()

    def bfs(x,y):
        q.append((x,y))
        visited[x][y]=1
        while q:
            xx,yy=q.popleft()
            for i in range(4):
                nx=xx+dx[i]
                ny=yy+dy[i]
                if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1:
                    q.append((nx,ny))
                    graph[nx][ny]=0
    result=0
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1:
                bfs(i,j)    
                result+=1

    print(result)