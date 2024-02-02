n=int(input())
graph=[[] for _ in range(n+1)]

result=[]

def dfs(v,i):
    visited[v]=1

    for x in graph[v]:
        if not visited[x]:
            dfs(x,i)
        elif visited[x]==1 and x==i:
            result.append(x)

for i in range(1,n+1):
    graph[int(input())].append(i)

for i in range(1,n+1):
    visited=[0]*(n+1)
    dfs(i,i)

result.sort()
print(len(result))
for r in result:
    print(r)

