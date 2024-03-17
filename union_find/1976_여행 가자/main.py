n=int(input())
m=int(input())
parent=[0]*(n+1)
for v in range(1,n+1):
    parent[v]=v
def find(parent,x):
    if parent[x]!=x:
        parent[x]=find(parent,parent[x])
    return parent[x]
def union_find(parent,a,b):
    a=find(parent,a)
    b=find(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

for i in range(n):
    temp=list(map(int,input().split()))  
    for j in range(n):
        if temp[j]==1:
            union_find(parent,i+1,j+1)

plan=list(map(int,input().split()))
root=find(parent,plan[0])
for i in range(1,m):
    if find(parent,plan[i])!=root:
        print('NO')
        break
else:
    print('YES')
