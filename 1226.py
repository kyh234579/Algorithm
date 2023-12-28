n=int(input())
arr=list(map(int,input().split()))
arr.sort()

ans=float("inf")

for i in range(n-3):
    for j in range(i+3,n):
        fix=arr[i]+arr[j]
        left=i+1
        right=j-1

        while left < right:
            s=arr[left] +arr[right]
            if abs(s-fix) < ans:
                ans=abs(s-fix)

            if s < fix:
                left+=1
            elif s > fix:
                right-=1
            else:
                print(0)
                exit(0)
print(ans)