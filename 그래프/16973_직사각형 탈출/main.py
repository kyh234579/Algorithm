from collections import deque
n,m=map(int,input().split())
maps=[list(map(int,input().split())) for _ in range(n)]
h,w,Sr,Sc,Fr,Fc=map(int,input().split())
Sr,Sc,Fr,Fc=Sr-1,Sc-1,Fr-1,Fc-1

#벽 리스트 만들기
walls=[]
for i in range(n):
    for j in range(m):
        if maps[i][j]==1:
            walls.append((i,j))
dr=[-1,1,0,0]
dc=[0,0,-1,1]
def move(r,c):
    queue=deque()
    queue.append((r,c))
    maps[r][c]=2
    while queue:
        nowr,nowc=queue.popleft()
        if nowr==Fr and nowc==Fc:
            return maps[nowr][nowc]-2
        for i in range(4):
            nr=nowr+dr[i]
            nc=nowc+dc[i]
            #범위 안에 있고, 방문이력이 없고, 직사각형 안에 벽이 없는 경우 -> True
            if 0<=nr<=n-h and 0<=nc<=m-w and maps[nr][nc]==0 and check(nr,nc):
                queue.append((nr,nc))
                maps[nr][nc]=maps[nowr][nowc]+1       
    return -1
#직사각형 안에 벽이 있는지 check하는 함수
def check(x,y):
    minx,maxx=x,x+h
    miny,maxy=y,y+w
    for (r,c) in walls:
        #벽이 있음
        if minx<= r <maxx and miny<= c <maxy:
            return False
    return True

print(move(Sr,Sc))
