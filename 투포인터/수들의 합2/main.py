n,m=map(int,input().split())
arr=list(map(int,input().split()))

end=0
n_sum=0
ans=0

for start in range(n):
    while n_sum<m and end<n:
        n_sum+=arr[end]
        end+=1
    if n_sum==m:
        ans+=1
    n_sum-=arr[start]

print(ans)