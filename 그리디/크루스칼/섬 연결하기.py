#부모 트리 찾기(재귀)
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]
#두 원소가 속한 집합 합치기 
def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)

    if a < b:
        parent[b] =a
    else:
        parent[a]=b

def solution(n,costs):
    parent=[0]*n #부모 테이블 초기화
#모든 간선을 담을 edges 리스트와 최종 비용을 담을 result 변수
    result=0
#부모 테이블 상에서 부모를 자기 자신으로 초기화
    for i in range(n):
        parent[i]=i
#비용순 정렬
    costs.sort(key=lambda x:x[2])
#간선 하나씩 확인
    for cost in costs:
        c,a,b = cost
    #사이클 발생하지 않을 때만 집합에 포함
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result+=c
    return result
    