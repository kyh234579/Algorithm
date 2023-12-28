n,k=map(int,input().split())
use=list(map(int,input().split()))
code=[]
answer=0

for this in range(k):
    #코드에 이미 꽂혀져 있음
    if use[this] in code:
        continue
    #코드 자리가 남음
    if len(code) < n:
        code.append(use[this])
        continue
    priority=[] #캐시
    for c in code:
        if c in use[this:]: #다음에 또 이용해야하는 거라면
            priority.append(use[this:].index(c))
        else: #아니면 101이라는 최대값을 넣어줌.
            priority.append(101)

    target=priority.index(max(priority))
    code.remove(code[target])
    code.append(use[this])
    answer+=1
print(answer)

