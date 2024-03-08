n,k=map(int,input().split())
s=list(map(int,input().split()))
k_cnt=0
end=0
ans=0
for start in range(n):
    while end < n:
        if s[end]%2==0:
            end+=1
        elif s[end]%2!=0 and k_cnt<k:
            k_cnt+=1
            end+=1
        else:
            break
    ans=max(ans,end-start-k_cnt)
    if s[start]%2!=0:
        k_cnt-=1

print(ans)
