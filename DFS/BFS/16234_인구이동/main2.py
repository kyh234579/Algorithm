from collections import deque
n,l,r=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    #연합할 나라 리스트
    union=[]
    union.append((x,y))
    while q:
        xx,yy=q.popleft()
        for i in range(4):
            nx=xx+dx[i]
            ny=yy+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n or visited[nx][ny]:
                continue
            #문제 조건대로 두 나라의 인구 차이가 l이상 r이하일때만, q에 넣어주고 bfs 탐색
            #union 리스트에도 추가
            if l<=abs(board[xx][yy]-board[nx][ny])<=r:
                q.append((nx,ny))
                union.append((nx,ny))
                visited[nx][ny]=1
    #이렇게 bfs 탐색했는데도, 연합할 나라가 없으면
    if len(union)==1:
        return 0
    #합계 계산해서 나라 갯수로 나눠준다음 그 값으로 인구 수 갱신
    ssum=0
    for i,j in union:
        ssum+=board[i][j]
    cc=ssum//len(union)
    for i,j in union:
        board[i][j]=cc
    #위 과정을 끝내면 1 반환
    return 1

day=0
while True:
    visited=[[0]*n for _ in range(n)]
    flag=0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j]=1
                flag+=bfs(i,j)
    #이제 더이상 연합할 나라가 존재하지않으면
    if flag==0:
        break
    day+=1

print(day)


