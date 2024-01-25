from collections import deque
n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]

#a가 b를 신뢰한다.b가 a의 부모이다.
#양방향이 아닌 단방향인 점 참고
for _ in range(m):
    a,b=map(int,input().split())
    graph[b].append(a)

def bfs(start):
    q=deque()
    q.append(start)

    visited=[False]*(n+1)
    visited[start]=True

    cnt=1
    while q:
        x=q.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i]=True
                q.append(i)
                cnt+=1
    return cnt
result=[]
for i in range(1,n+1):
    result.append(bfs(i))
for i in range(n):
    if max(result)==result[i]:
        print(i+1,end=' ')                                                                                             