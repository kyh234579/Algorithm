from collections import deque
n=int(input())
arr=list(map(int,input().split()))
arr.sort()
lst=deque()
for a in arr:
    lst.append(a)
ans=0
while len(lst)>1:
    ans+=1
    min=lst.popleft()
    max=lst.pop()
    if min !=1:
        lst.appendleft(min-1)

print(ans)
