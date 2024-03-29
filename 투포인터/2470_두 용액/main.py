n=int(input())
arr=list(map(int,input().split()))
arr.sort()
left=0
right=n-1

result=abs(arr[left]+arr[right])
final=[arr[left],arr[right]]

while left < right:
    sumA=arr[left]+arr[right]

    if abs(sumA) < result:
        result=abs(sumA)
        final[0]=arr[left]
        final[1]=arr[right]
        if result ==0:
            break
    #더한값이 음수면, left가 0에서 너무 먼값이기 때문에
    if sumA<0:
        left+=1
    else:
        right-=1

print(final[0],final[1])