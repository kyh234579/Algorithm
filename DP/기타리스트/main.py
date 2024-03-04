n,s,m=map(int,input().split())
v=list(map(int,input().split()))
#dp[i][j]-> i번째 곡을 j만큼의 볼륨으로 연주할 수 있는지 여부
dp=[[0]*(m+1) for _ in range(n+1)]
#첫시작 볼륨
dp[0][s]=1

for i in range(n):
    for j in range(m+1):
        if dp[i][j]==1:
            min_val=j-v[i]
            max_val=j+v[i]
            if min_val>=0:
                dp[i+1][min_val]=1
            if max_val<=m:
                dp[i+1][max_val]=1

result=-1
for i in range(m,-1,-1):
    if dp[n][i]==1:
        result=max(result,i)

print(result)