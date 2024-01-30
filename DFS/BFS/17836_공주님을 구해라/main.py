from collections import deque
n,m,t=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
visited=[[False]*m for _ in range(n)]
q=deque()
#x,y,depth까지 저장
q.append((0,0,0))
#거리 min 비교할 최대값 설정
result=1e9

dx=[-1,1,0,0]
dy=[0,0,-1,1]
while q:
    x,y,d=q.popleft()
    if x==n-1 and y==m-1:
        #그람을 통해 간 거리와 그냥 간 거리 둘을 비교해서 최소값 출력
        result=min(result,d)
        break
    if d >= t:
        break
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        #범위 확인
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            if board[nx][ny]==0:
                visited[nx][ny]=True
                q.append((nx,ny,d+1))
            #그람 발견
            elif board[nx][ny]==2:
                visited[nx][ny]=True
                temp=d+1+abs(n-1-nx)+abs(m-1-ny)
                if temp <= t:
                    result=temp

if result > t:
    print('Fail')
else:
    print(result)