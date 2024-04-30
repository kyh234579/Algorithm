from collections import deque
graph=[]
for _ in range(12):
    temp=list(input().rstrip())
    graph.append(temp)

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def check(x,y):
    q=deque()
    q.append((x,y))
    now=graph[x][y]
    #같은 색 뿌요 갯수 세기용
    pos=[]
    while q:
        xx,yy=q.popleft()
        for i in range(4):
            nx=xx+dx[i]
            ny=yy+dy[i]
            if 0<=nx<12 and 0<=ny<6 and not visited[nx][ny] and now==graph[nx][ny]:
                q.append((nx,ny))
                pos.append((nx,ny))
                visited[nx][ny]=1
    if len(pos)>=4:
        #같은 열을 기준으로 정렬 후, 행 오름차순
        #(10,0),(11,0) -> (10,0)을 먼저 빼서 내리기 시행을 위해
        pos.sort(key=lambda x:(x[1],x[0]))
        for i,j in pos:
            graph[i][j]='_'
            bomblist.append((i,j))
ans=0
while True:
    visited=[[0]*6 for _ in range(12)]
    #터진 뿌요 담기
    bomblist=[]
    for i in range(12):
        for j in range(6):
            if graph[i][j]!='.' and graph[i][j]!='_' and not visited[i][j]:
                check(i,j)
    
    #이제 더이상, 터트릴 뿌요가 없다면
    if len(bomblist) == 0:
        break
    
    #뿌요 내리기
    for x,y in bomblist:
        for i in range(x,0,-1):
            graph[i][y]=graph[i-1][y]
        #y열 기준 뿌요 내리기 완료 후, 무조건 맨 위에있는 건 '.'이 되어야함
        graph[0][y]='.'

    ans+=1

print(ans)
                
    