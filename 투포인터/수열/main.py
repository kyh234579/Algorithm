n,k=map(int,input().split())
nums=list(map(int,input().split()))
part_sum=sum(nums[:k])
answer=part_sum
for i in range(n-k):
    part_sum+=nums[i+k]-nums[i]
    if part_sum > answer:
        answer=part_sum
print(answer)