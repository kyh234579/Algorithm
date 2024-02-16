h,w=map(int,input().split())
array=list(map(int,input().split()))

result=0
for i in range(1,w-1):
    left_max=max(array[:i])
    right_max=max(array[i+1:])

    compare=min(left_max,right_max)

    if array[i] < compare:
        result+=compare-array[i]

print(result)