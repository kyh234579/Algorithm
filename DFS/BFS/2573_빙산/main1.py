from collections import deque

n,m=map(int,input().split())
map=[list(map(int,input().split())) for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

#주변 바다 갯수 만큼 -1 해주고, 그룹 체크하기
def bfs(x,y):
    q=deque()
    q.append([x,y])
    visited[x][y]=1
    while q:
        xx,yy=q.popleft()
        for i in range(4):
            nx=xx+dx[i]
            ny=yy+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m or visited[nx][ny]:
                continue
            #바다 이면
            if map[nx][ny]==0:
                #빙산의 높이가 음수가 되면 안되기때문
                map[xx][yy]=max(0,map[xx][yy]-1)
            else:
                visited[nx][ny]=1
                q.append([nx,ny])

    return 1

#빙산 담기
ice=[]
for i in range(n):
    for j in range(m):
        if map[i][j]!=0:
            ice.append((i,j))

total_time=0
while ice:
    visited=[[0]*m for _ in range(n)]
    dellist=[]
    group=0
    for i,j in ice:
        if not visited[i][j]:
            group+=bfs(i,j)
        #하나의 빙산이 다 녹았으면 dellist에 담기
        if map[i][j]==0:
            dellist.append((i,j))
    if group>1:
        print(total_time)
        break
    #기존 ice에서 녹아서 없어진 빙산들, dellist를 제외해줌.
    ice=sorted(list(set(ice)-set(dellist)))
    total_time+=1

#빙산이 다 녹을때까지 두 동강이 나지 않았으면
if group==1:
    print(0)