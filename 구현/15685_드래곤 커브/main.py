n=int(input())
#시작 방향
dx=[0,-1,0,1]
dy=[1,0,-1,0]
visited=[[0]*101 for _ in range(101)]

for _ in range(n):
    y,x,d,g=map(int,input().split())
    #0세대 생성
    visited[x][y]=1
    #커브리스트 생성
    curve=[d]
    for j in range(g):
        for k in range(len(curve)-1,-1,-1):
            curve.append((curve[k]+1)%4)
    #드래곤 커브 만들기
    for j in range(len(curve)):
        x+=dx[curve[j]]
        y+=dy[curve[j]]
        if x <0 or y <0 or x>=101 or y>=101:
            continue
        visited[x][y]=1

result=0
#격자의 크기는 100*100이므로, 0~99까지 탐색해야함
for i in range(100):
    for j in range(100):
        if visited[i][j]==1 and visited[i][j+1]==1 and visited[i+1][j+1]==1 and visited[i+1][j]==1:
            result+=1
print(result)
