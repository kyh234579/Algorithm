from collections import deque
n,m=map(int,input().split())
board=[list(map(int,input())) for _ in range(n)]
#visited[x][y][w]라는 3차원 리스트 생성
#w=0은 벽을 부수지 않은 경우
#w=1은 벽을 한번이라도 부순 경우
visited=[[[0,0] for _ in range(m)] for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs():
    queue=deque()
    queue.append([0,0,0])
    visited[0][0][0]=1    
    while queue:
        x,y,w=queue.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][w]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                #현재 위치로 이동 가능하고 방문하지 않았다면 
                if board[nx][ny]==0 and visited[nx][ny][w]==0:
                    visited[nx][ny][w]=visited[x][y][w]+1
                    queue.append([nx,ny,w])
                #현재 위치가 벽이고 한번도 부신적이 없다면
                elif board[nx][ny] ==1 and w == 0:
                    visited[nx][ny][w+1]=visited[x][y][w]+1
                    queue.append([nx,ny,w+1])

    return -1

print(bfs())