n=int(input())
times=list(map(int,input().split()))
times.sort()
#1 2 3 3 4
tmp=0
for i in range(1,n+1):
    tmp+=sum(times[:i])

print(tmp)