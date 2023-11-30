n=int(input())
roads=list(map(int,input().split()))
costs=list(map(int,input().split()))
minPrice=costs[0]
total=0
for i in range(n-1):
    if minPrice > costs[i]:
        minPrice=costs[i]
    total+=(minPrice*roads[i])
print(total)