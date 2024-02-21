from collections import deque
n=int(input())
space=[]
for _ in range(n):
    temp=list(map(int,input().split()))
    space.append(temp)
start_idx=[]
for i in range(n):
    for j in range(n):
        if space[i][j]==9:
            start_idx.append(i)
            start_idx.append(j)
#bfs로 거리계산하고 이동하며 후보리스트 만들기
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(x,y):
    q=deque()
    q.append((x,y))
    cand=[]
    visited=[[0]*n for _ in range(n)]
    visited[x][y]=1
    while q:
        i,j=q.popleft()
        for k in range(4):
            ii=i+dx[k]
            jj=j+dy[k]
            if ii<0 or jj<0 or ii>=n or jj>=n or visited[ii][jj]!=0:
                continue
            #이동 상세조건
            #물고기 후보리스트
            if space[x][y] > space[ii][jj] and space[ii][jj]!=0:
                visited[ii][jj]=visited[i][j]+1
                cand.append((visited[ii][jj]-1,ii,jj))
            #지나가는 것만 가능
            elif space[x][y] == space[ii][jj] or space[ii][jj]==0:
                visited[ii][jj]=visited[i][j]+1
                q.append((ii,jj))
    cand.sort(key=lambda x:(x[0],x[1],x[2]))
    return cand

#cand=[(거리,x,y)]
i,j=start_idx
size=[2,0]
cnt=0
while True:
    space[i][j]=size[0]
    cand=bfs(i,j)
    if not cand:
        break
    step,xx,yy=cand.pop(0)
    cnt+=step
    size[1]+=1
    if size[0]==size[1]:
        size[0]+=1
        size[1]=0
    space[i][j]=0
    i,j=xx,yy

print(cnt)
    




