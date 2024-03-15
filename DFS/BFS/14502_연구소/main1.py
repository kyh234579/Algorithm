from collections import deque
from itertools import combinations
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(graph):
    q=deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j]==2:
                q.append((i,j))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
                graph[nx][ny]=2
                q.append((nx,ny))
    cnt=0
    for i in range(n):
        cnt+=graph[i].count(0)
    return cnt

n,m=map(int,input().split())
initgraph=[]
blank=[]
result=0
for i in range(n):
    temp=list(map(int,input().split()))
    for j in range(m):
        if temp[j]==0:
            blank.append((i,j))
    initgraph.append(temp)

wall_comb=combinations(blank,3)

for wall in wall_comb:
    #매번 새로운 조합의 3개의 벽을 세울때마다 초기 그래프를 가지고 시행해야함으로 초기 그래프 복사해줌.
    #2차원 배열 복사 -> deepcopy or 슬라이싱 사용, 슬라이싱이 시간 덜 소요
    temp_graph=[g[:] for g in initgraph]
    for x,y in wall:
        temp_graph[x][y]=1
    result=max(result,bfs(temp_graph))

print(result)
