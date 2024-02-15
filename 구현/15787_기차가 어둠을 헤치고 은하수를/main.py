n,m=map(int,input().split())
graph=[]
for _ in range(n+1):
    graph.append([0]*21)

for _ in range(m):
    a=list(map(int,input().split()))
    if a[0]==1:
        if graph[a[1]][a[2]]==0:
            graph[a[1]][a[2]]=1
    if a[0]==2:
        if graph[a[1]][a[2]]==1:
            graph[a[1]][a[2]]=0
    if a[0]==3:
        graph[a[1]][20]=0
        for k in range(19,0,-1):
            if graph[a[1]][k]==1:
                graph[a[1]][k]=0
                graph[a[1]][k+1]=1
    if a[0]==4:
        graph[a[1]][1]=0
        for k in range(2,21):
            if graph[a[1]][k]==1:
                graph[a[1]][k]=0
                graph[a[1]][k-1]=1

#명령 후 은하수 건너기
result=[]
for i in range(1,n+1):
    if graph[i] in result:
        continue
    result.append(graph[i])
print(len(result))

                