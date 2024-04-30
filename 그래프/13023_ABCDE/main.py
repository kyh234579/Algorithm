n,m=map(int,input().split())
graph=[[] for _ in range(n)]
answer=False
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v,depth):
    global answer
    visited[v]=1
    if depth==4:
        answer=True
        return
    for x in graph[v]:
        if not visited[x]:
            dfs(x,depth+1)
    #이미 방문한 노드는, 취소 처리 -> 백트래킹
    visited[v]=0

for i in range(n):
    visited=[0]*n
    #첫 노드부터 차례대로 dfs 수행해주고, 하나라도 depth=4가 충족된 경우 바로 break
    dfs(i,0)
    if answer:
        break
if answer:
    print(1)
else:
    print(0)
