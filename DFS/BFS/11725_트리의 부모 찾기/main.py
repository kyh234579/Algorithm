import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline()  
n=int(input()) 
visited=[0]*(n+1)
graph=[[] for _ in range(n+1)]

for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    for x in graph[v]:
        if visited[x]==0:
            visited[x]=v
            dfs(x)
dfs(1)
for i in range(2,n+1):
    print(visited[i])
