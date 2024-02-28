n=int(input())
nums=list(map(int,input().split()))
#+,-,*,//
operators=list(map(int,input().split()))
max_value=-1000000000
min_value=1000000000
def dfs(idx,sum,add,sub,mul,div):
    global max_value,min_value
    #가지치기
    if idx==n:
        min_value=min(min_value,sum)
        max_value=max(max_value,sum)  
        return
    if add:
        dfs(idx+1,sum+nums[idx],add-1,sub,mul,div)
    if sub:
        dfs(idx+1,sum-nums[idx],add,sub-1,mul,div)
    if mul:
        dfs(idx+1,sum*nums[idx],add,sub,mul-1,div)
    if div:
        dfs(idx+1,int(sum/nums[idx]),add,sub,mul,div-1)

dfs(1,nums[0],operators[0],operators[1],operators[2],operators[3])

print(max_value)
print(min_value)

