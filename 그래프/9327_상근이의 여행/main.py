import sys
input=sys.stdin.readline

T=int(input())

def dfs(v,cnt):
    global graph
    visited[v]=1
    for node in graph[v]:
        if not visited[node]:
            cnt=dfs(node,cnt+1)
    return cnt    

for _ in range(T):
    result=0
    n,m=map(int,input().split())
    graph=[[] for _ in range(n+1)]
    visited=[0]*(n+1)
    visited[0]=1
    for _ in range(m):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    result=dfs(1,0)
    print(result)

