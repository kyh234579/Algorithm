n,m=map(int,input().split())
#진실을 알고 있는 사람들의 번호
truth=list(map(int,input().split()))[1:]
#부모 노드 만들기
parent=[0]*(n+1)
for v in range(n+1):
    parent[v]=v    

def find(parent,x):
    if parent[x]!= x:
        parent[x]=find(parent,parent[x])
    return parent[x]

def union_find(parent,a,b):
    a=find(parent,a)
    b=find(parent,b)
    #만약 둘의 부모노드가 모두 truth에 포함된다면, union연산 생략
    if a in truth and b in truth:
        return 
    elif a in truth:
        parent[b]=a
    elif b in truth:
        parent[a]=b
    #둘다 포함되지 않는다면, 원래 union 공식대로 값이 작은게 부모노드가 되게끔
    else:
        if a<b:
            parent[b]=a
        else:
            parent[a]=b
parties=[]
for _ in range(m):
    temp=list(map(int,input().split()))
    party_len=temp[0]
    party=temp[1:]
    for i in range(party_len-1):
        union_find(parent,party[i],party[i+1])
    parties.append(party)
ans=0
for party in parties:
    for i in range(len(party)):
        if find(parent,party[i]) in truth:
            break
    else:
        ans+=1
print(ans)