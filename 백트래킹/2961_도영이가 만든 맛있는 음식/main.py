n=int(input())
ingredients=[]
for _ in range(n):
    s,b=map(int,input().split())
    ingredients.append([s,b])

min_value=1e9
def dfs(idx,a,b,cnt):
    global min_value
    #가지치기
    if idx==n:
        if cnt>0:
            min_value=min(min_value,abs(a-b))
        return
    #본인포함
    dfs(idx+1,a*ingredients[idx][0],b+ingredients[idx][1],cnt+1)
    #미포함,인덱스만 증가시켜 다음재료로 넘어감.
    dfs(idx+1,a,b,cnt)

dfs(0,1,0,0)
print(min_value)