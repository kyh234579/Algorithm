from collections import deque
from itertools import combinations
import copy
n,m=map(int,input().split())

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(graph):
    queue=deque()
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                queue.append((i,j))
        
    while queue:
        x,y=queue.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx < 0 or ny < 0 or nx >=n or ny >=m:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny]=2
                queue.append((nx,ny))

    result=0
    for i in range(n):
        result+=graph[i].count(0)
    return result

board=[]
blank=[]
result=0
for i in range(n):
    temp=list(map(int,input().split()))
    for j in range(m):
        if temp[j] == 0:
            blank.append((i,j))
    board.append(temp)

nCr = combinations(blank,3)

for x in nCr:
    temp_board=copy.deepcopy(board) #원래 그래프 상태로 초기화
    for i, j in x:
        temp_board[i][j] = 1
    result=max(result,bfs(temp_board))

print(result)