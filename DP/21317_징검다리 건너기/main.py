import sys
input = sys.stdin.readline
n=int(input())
arr=[]
dp=[1e9]*n
dp[0]=0
#dp배열 만들기(최소값 에너지 갱신), 작은 점프, 큰 점프와 같은 두가지 경우만 고려
for i in range(n-1):
    a,b=map(int,input().split())
    arr.append((a,b))
    if i+1 < n: dp[i+1]=min(dp[i+1],dp[i]+a)
    if i+2 < n: dp[i+2]=min(dp[i+2],dp[i]+b)
    
_min = dp[-1] #두 경우만 고려한, 마지막 돌까지의 에너지
k=int(input())

#dp 안 모든 경우에 매우 큰 점프를 적용하여 최소값 갱신.

for i in range(3,n):
    e,dp1,dp2 = dp[i-3]+k,1e9,1e9
    for j in range(i,n-1):
        if i+1 <=n: dp1=min(dp1,e+arr[j][0])
        if i+2 <=n: dp2=min(dp2,e+arr[j][1])
        e,dp1,dp2=dp1,dp2,1e9
    _min=min(_min,e)
print(_min)
