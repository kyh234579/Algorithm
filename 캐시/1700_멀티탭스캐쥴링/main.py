n,k=map(int,input().split())
use=list(map(int,input().split()))
code=[]
answer=0

for this in range(k):
    if use[this] in code:
        continue
    if len(code) < n:
        code.append(use[this])
        continue
    priority=[]
    for c in code:
        if c in use[this:]:
            priority.append(use[this:].index(c))
        else:
            priority.append(101)
    target=priority.index(max(priority))
    code.remove(code[target])
    code.append(use[this])
    answer+=1
print(answer)