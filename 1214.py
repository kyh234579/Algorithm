from itertools import combinations

N,M=map(int,input().split())
arr=list(map(int,input().split()))
ans=[]
for c in combinations(arr,3):
    if sum(c) <= M:
        ans.append(c)
ans.sort(key=lambda x:sum(x))

print(sum(ans[-1]))