from collections import deque
n=int(input())
board=[list(input().rstrip()) for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(x,y):
    q=deque()
    q.append((x,y))
    now=board[x][y]
    visited[x][y]=1
    while q:
        xx,yy=q.popleft()
        for i in range(4):
            nx=xx+dx[i]
            ny=yy+dy[i]
            if 0<=nx<n and 0<=ny<n and board[nx][ny]==now and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny]=1

visited=[[0]*n for _ in range(n)]
cnt=0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            cnt+=1
#적록색약 인경우
for i in range(n):
    for j in range(n):
        if board[i][j]=='R':
            board[i][j]='G'

visited=[[0]*n for _ in range(n)]
cnt_1=0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            cnt_1+=1
print(cnt,cnt_1)
