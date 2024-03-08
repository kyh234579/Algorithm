n,s=map(int,input().split())
arr=list(map(int,input().split()))
sum=arr[0]
min_length=float("inf")
left,right=0,0

while left <= right:
    if sum >=s:
        min_length=min(min_length,right-left+1)
        sum-=arr[left]
        left+=1
    else:
        right+=1    
        if right < n:
            sum+=arr[right]
        else:
            break
        
if min_length == float("inf"):
    print(0)
else:
    print(min_length)