#두 노드의 거리가 가장 큰 값 구하기
#1) 1(루트노드)로 시작해서 가장 먼 노드 구하기
#2) 이 노드를 시작점으로 해서, 다시 가장 먼 노드까지의 거리 구하기
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

n=int(input())
graph=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,value=map(int,input().split())
    graph[a].append((b,value))
    graph[b].append((a,value))

#1)
def dfs(start,distance):
    for next,next_d in graph[start]:
        if visited[next]==-1:
            visited[next]=distance+next_d
            dfs(next,distance+next_d)

visited=[-1]*(n+1)
visited[1]=0
dfs(1,0)

#2)
last_node=visited.index(max(visited))
visited=[-1]*(n+1)
visited[last_node]=0
dfs(last_node,0)

print(max(visited))

