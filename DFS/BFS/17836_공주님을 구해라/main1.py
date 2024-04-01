from collections import deque
n,m,t=map(int,input().split())
map=[list(map(int,input().split())) for _ in range(n)]
visited=[[-1]*m for _ in range(n)]

q=deque()
q.append([0,0])
visited[0][0]=0
dx=[-1,1,0,0]
dy=[0,0,-1,1]
min_time=1e9
while q:
    x,y=q.popleft()
    if x==n-1 and y==m-1:
        #칼을 사용하고 공주까지 간 거리와 그냥 간 거리 둘 중의 최소값 구하기
        min_time=min(min_time,visited[n-1][m-1])
        break
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=m or visited[nx][ny]!=-1:
            continue
        if map[x][y]==2:
            #칼까지의 최단 거리+칼에서 공주까지의 거리
            min_time=min(min_time,visited[x][y]+n-1-x+m-1-y)
        if map[nx][ny] == 0:
            visited[nx][ny]=visited[x][y]+1
            q.append([nx,ny])   
        if map[nx][ny]==2:
            visited[nx][ny]=visited[x][y]+1
            q.appendleft([nx,ny])
            
if 0<min_time<=t:
    print(min_time)
else:
    print('Fail')