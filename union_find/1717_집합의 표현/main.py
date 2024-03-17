import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**7)
n,m=map(int,input().split())
parent=[0]*(n+1)
for i in range(1,n+1):
    parent[i]=i
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

for _ in range(m):
    tmp,a,b=map(int,input().split())
    if tmp==0:
        union_find(parent,a,b)
    elif tmp==1:
        if find(parent,a) == find(parent,b):
            print('YES')
        else:
            print('NO')