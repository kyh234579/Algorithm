n,m=map(int,input().split())
data=[list(map(int,input().split())) for _ in range(n)]
mins=[]
for a in data:
    mins.append(min(a))
print(max(mins))