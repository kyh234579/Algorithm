n=int(input())
prices=[]
visited=[[0]*n for _ in range(n)]
for _ in range(n):
    temp=list(map(int,input().split()))
    prices.append(temp)
dx=[0,-1,1,0,0]
dy=[0,0,0,-1,1]

def check(x,y):
    for i in range(5):
        nx=x+dx[i]
        ny=y+dy[i]
        if visited[nx][ny] == 1:
            return False
    return True
cnt=0
total=0
answer=1e9
def dfs(cnt):
    global answer,total
    if cnt==3:
        answer=min(answer,total)
        return
    for i in range(1,n-1):
        for j in range(1,n-1):
            if check(i,j):
                for k in range(5):
                    ii=i+dx[k]
                    jj=j+dy[k]
                    visited[ii][jj]=1
                    total+=prices[ii][jj]
                dfs(cnt+1)
                #백트래킹, 방문 취소 후, 다시 진행
                for k in range(5):
                    ii=i+dx[k]
                    jj=j+dy[k]
                    visited[ii][jj]=0
                    total-=prices[ii][jj]
dfs(0)
print(answer)


        
