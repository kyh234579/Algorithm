n,m=map(int,input().split())
board=[]
for _ in range(n):
    temp=list(map(int,input().split()))
    board.append(temp)
gurem_idx=[(n-2,0),(n-2,1),(n-1,0),(n-1,1)]
#8방향
dx=[0,-1,-1,-1,0,1,1,1]
dy=[-1,-1,0,1,1,1,0,-1]
for _ in range(m):
    d,s=map(int,input().split())
    visited=[[False]*n for _ in range(n)]
    while gurem_idx:
        x,y=gurem_idx.pop(0)
        #1단계
        nx=(x+s*dx[d-1])%n
        ny=(y+s*dy[d-1])%n
        #구름 위치 체크
        visited[nx][ny]=True 
    #2단계, 구름 모두 이동이 끝난 후, 물양 추가
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                board[i][j]+=1
    #4단계, 구름 위치 찾아서 대각선에 물이 담긴 바구니 개수 체크
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                for k in range(1,8,2):
                    d_x=i+dx[k]
                    d_y=j+dy[k]
                    if d_x < 0 or d_y<0 or d_x>=n or d_y>=n:
                        continue
                    if board[d_x][d_y]>0:
                        board[i][j]+=1
    #5단계
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            if board[i][j]>=2:
                board[i][j]-=2
                gurem_idx.append((i,j))

result=0
for i in range(n):
    result+=sum(board[i])
print(result)