from collections import deque
m,n=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]

queue=deque()

#익은 토마토 index를 queue에 차례대로 넣기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i,j))

#꺼내서 bfs수행하면서 4방향 탐색
def bfs():
    while queue:
        x,y=queue.popleft()
        dx=[-1,1,0,0]
        dy=[0,0,-1,1]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))

bfs()
day=0
for row in graph:
    for i in row:
        if i==0:
            print(-1)
            exit()
    #한 행의 최대값이 그 행에서 가장 늦게 익은 토마토이기 때문에 , 뽑아서 각 행마다 비교. 하고 최대값 뽑아내기
    day=max(max(row),day)

#처음에 1로 시작해서 +1 했으므로, -1을 해줘야 정답
print(day-1)