#부모 노드 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

#union 연산, 합치기
def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a < b:
        parent[b]=a
    else:
        parent[a]=b

#노드, 간선 개수 입력 받기
v,e=map(int,input().split())
parent=[0]*(v+1)
#노드들의 정보, 총 비용 초기화
edges=[]
all_cost=0
#부모 노드 리스트 본인 값으로 초기화
for i in range(1,v+1):
    parent[i] = i
#간선 정보 입력받기
for _ in range(e):
    a,b,cost=map(int,input().split())
    edges.append((a,b,cost))

edges.sort(key=lambda x: x[2])

for edge in edges:
    a,b,cost=edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        all_cost+=cost

print(all_cost)
