n,m=map(int,input().split())
truth=list(map(int,input().split()))[1:]
parent=[0]*(n+1)
for i in range(1,n+1):
    parent[i]=i

def find(parent,x):
    #루트노드가 아니라면, 다시 부모노드 찾기
    if x!=parent[x]:
        parent[x]=find(parent,parent[x])
    return parent[x]

def union_find(parent,a,b,truth):
    a=find(parent,a)
    b=find(parent,b)

    if a in truth and b in truth:
        return
    elif a in truth:
        parent[b]=a
    elif b in truth:
        parent[a]=b
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
        union_find(parent,party[i],party[i+1],truth)
    parties.append(party)
ans=0
for party in parties:
    for i in range(len(party)):
        if find(parent,party[i]) in truth:
            break
    else:
        ans+=1

print(ans)
