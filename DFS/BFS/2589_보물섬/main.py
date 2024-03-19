import sys
input=sys.stdin.readline

from collections import deque
n,m=map(int,input().split())
board=[list(input().rstrip()) for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    visited=[[0]*m for _ in range(n)]
    visited[x][y]=1
    cnt=0
    while q:
        xx,yy=q.popleft()
        for i in range(4):
            nx=xx+dx[i]
            ny=yy+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m or visited[nx][ny]:
                continue
            if board[nx][ny]=='L':
                q.append((nx,ny))
                visited[nx][ny]=visited[xx][yy]+1
                cnt=max(cnt,visited[nx][ny])
    return cnt-1


result=0
for i in range(n):
    for j in range(m):
        if board[i][j]=='L':
            result=max(result,bfs(i,j))

print(result)