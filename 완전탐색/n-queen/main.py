n=int(input())
col=[0]*n
visited=[0]*n
def check(x):
    for i in range(x):
        #열이 같거나, 대각선 위치에 퀸이 있다면 
        if col[i]==col[x] or abs(x-i)==abs(col[x]-col[i]):
            return False
    return True
answer=0
def dfs(x):
    global answer
    #가지치기
    if x==n:
        answer+=1
        return
    for i in range(n):
        if visited[i]!=0:
            continue
        #[x,i]에 퀸을 놓음
        col[x]=i
        #해당 위치에 퀸을 놓을 수 있다면
        if check(x):
            visited[i]=1
            dfs(x+1)
            visited[i]=0
                     
dfs(0)
print(answer)
