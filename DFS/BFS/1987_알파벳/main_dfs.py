import sys
sys.setrecursionlimit(10**7)
r,c=map(int,input().split())
board=[list(input().rstrip()) for _ in range(r)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def dfs(x,y,cnt):
    global max_cnt
    max_cnt=max(max_cnt,cnt)
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or ny<0 or nx>=r or ny>=c or visited[ord(board[nx][ny])-ord('A')]:
            continue
        visited[ord(board[nx][ny])-ord('A')]=1
        dfs(nx,ny,cnt+1)
        visited[ord(board[nx][ny])-ord('A')]=0

visited=[0]*26
visited[ord(board[0][0])-ord('A')]=1
max_cnt=1
dfs(0,0,1)
print(max_cnt)