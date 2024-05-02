from collections import deque
n,m=map(int,input().split())
init=[deque(),deque()]
dumi=[deque(),deque()]
for _ in range(n):
    a,b=map(int,input().split())
    init[0].appendleft(a)
    init[1].appendleft(b)

t=0
for _ in range(m):
    dumi[t].appendleft(init[t].popleft())
    #도중에 자신의 덱에 아무것도 없다면
    if not init[t]:
        break
    winner=-1
    #둘 중 하나가 5라면
    for i in [0,1]:
        if dumi[i] and dumi[i][0]==5:
            winner=0
    #더미 맨 위 숫자의 합이 5라면
    if dumi[0] and dumi[1] and dumi[0][0]+dumi[1][0]==5:
        winner=1
    if winner!=-1:
        for k in [1-winner,winner]:
            while dumi[k]:
                init[winner].append(dumi[k].pop())
    t=1-t
if len(init[0])>len(init[1]):
    print('do')
elif len(init[0])<len(init[1]):
    print('su')
else:
    print('dosu')