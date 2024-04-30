n,k=map(int,input().split())
a=list(map(int,input().split()))
answer=0
start,end=0,0
counter=[0]*(max(a)+1)

while end<n:
    if counter[a[end]] <k:
        counter[a[end]]+=1
        end+=1
    else:
        counter[a[start]]-=1
        start+=1
    answer=max(answer,end-start)

print(answer)
