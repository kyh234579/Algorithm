from itertools import combinations

n=int(input())
cost=list(map(int,input().split()))
n_list=[i for i in range(1,n+1)]

case_list=[] #조합 연산을 통해 담을 모든 선거구 케이스

for i in range(1,(n//2)+1):
    first=list(combinations(n_list,i))
    for j in first:
        last=list(set(n_list)-set(j))
        case_list.append((list(j),last))

#인접 리스트 만들기
graph=[[] for _ in range(n+1)]

for i in range(1,n+1):
    tempt=list(map(int,input().split()))
    adja=tempt.pop(0)
    for j in tempt:
        if j not in graph[i]:
            graph[i].append(j)
            graph[i].sort()
        if i not in graph[j]:
            graph[j].append(i)
            graph[j].sort()

def dfs(v,visited,elem):
    visited[v]=True
    for i in graph[v]:
        if not visited[i] and i in elem:
            dfs(i,visited,elem)
ans=1e9
#case_list에 dfs 적용해서 인접 확인하기(visited)
for case in case_list:
    first=case[0]
    last=case[1]

    first_visited=[False]*(n+1)
    last_visited=[False]*(n+1)

    dfs(first[0],first_visited,first)
    dfs(last[0],last_visited,last)

    check=False

    for i in first:
        if not first_visited[i]:
            check=True
    for i in last:
        if not last_visited[i]:
            check=True
    #하나라도 방문하지 않은 노드가 있다면, 생략(넘어감)
    if check:
        continue

    #만약 성공시 first/last 각 cost 총계 구하기
    sum_first=0
    sum_last=0

    for i in first:
        sum_first+=cost[i-1]
    for i in last:
        sum_last+=cost[i-1]

    ans_check=abs(sum_first-sum_last)
    ans=min(ans,ans_check)

if ans==1e9:
    print(-1)
else:
    print(ans)
