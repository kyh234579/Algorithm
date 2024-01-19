n=int(input())
m=int(input())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
#인접 정보 리스트 생성
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

#재귀 방문
def dfs(v):
    visited[v]=True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

dfs(1)
result=0 
for i in range(n+1):
    if visited[i]:
        result+=1
print(result-1)