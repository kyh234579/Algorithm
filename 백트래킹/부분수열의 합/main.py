n,s=map(int,input().split())
nums=list(map(int,input().split()))

result=0
def dfs(idx,sum,cnt):
    global result
    if idx==n:
        if cnt>0 and sum==s:
            result+=1
        return
    #본인 포함
    dfs(idx+1,sum+nums[idx],cnt+1)
    #본인 미포함
    dfs(idx+1,sum,cnt)

dfs(0,0,0)
print(result)