from collections import deque
n,m=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

q=deque()

def bfs(x,y):
    q.append((x,y))
    visited[x][y]=True
    seaList=[]
    while q:
        x,y=q.popleft()
        sea=0
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx <0 or nx >=n or ny<0 or ny>=m:
                continue
            if board[nx][ny] !=0 and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny]=True
            if board[nx][ny]==0:
                sea+=1  
        if sea>0:
            seaList.append((x,y,sea))
    for x,y,sea in seaList:
        #0이상이어야하기 때문에
        board[x][y]=max(0,board[x][y]-sea)

    #그룹 체크
    return 1

#main
#빙산 체크
ice=[]
for i in range(n):
    for j in range(m):
        if board[i][j]:
            ice.append((i,j))
year=0
while ice:
    visited=[[False]*m for _ in range(n)]
    delList=[]
    group=0
    for i,j in ice:
        if board[i][j] and not visited[i][j]:
            group+=bfs(i,j)
        #시행후 다 녹아버린 빙산
        if board[i][j]==0:
            delList.append((i,j))
    
    if group >1:
        print(year)
        break
    ice=sorted(list(set(ice)-set(delList)))
    year+=1

if group == 1:
    print(0)


            
    


