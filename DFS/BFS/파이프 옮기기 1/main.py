n=int(input())
map=[list(map(int,input().split(' '))) for _ in range(n)]

ans=0

def dfs(x,y,dir):
    global ans
    if x==n-1 and y==n-1:
        ans+=1
        return
    #대각선으로 갈 수 있다면 대각선으로 먼저 이동하기
    if x+1<n and y+1<n:
        #벽을 긁지 않아야해서
        if map[x+1][y+1]==0 and map[x+1][y]==0 and map[x][y+1]==0:
            dfs(x+1,y+1,2) 
    #가로나 대각선일 때, 가로로 이동
    if dir==0 or dir==2:
        #가로로 이동할 수 있으면
        if y+1<n and map[x][y+1]==0:
            dfs(x,y+1,0)
    #세로나 대각선일 때, 세로로 이동
    if dir==1 or dir==2:
        if x+1<n and map[x+1][y]==0:
            dfs(x+1,y,1)
#대가리 기준으로 x,y 그리고 마지막은 현 상태. 0->가로, 1->세로, 2->대각선
dfs(0,1,0)

print(ans)

        