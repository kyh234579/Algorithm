n=int(input())
arr=list(map(int,input().split()))
m=int(input())
cnt =0
for _ in range(m):
    arr[0]+=1
    arr[n-1]-=1
    arr.sort()

print(arr[n-1] - arr[0])

    