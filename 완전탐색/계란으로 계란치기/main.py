import sys
sys.setrecursionlimit(10*7)
n=int(input())
eggs=[]
for _ in range(n):
    s,w=map(int,input().split())
    eggs.append([s,w])
def dfs(start):
    global answer
    if start==n:
        total=0
        for i in range(n):
            if eggs[i][0]<=0:
                total+=1
        answer=max(answer,total)    
        return
    #제한사항 1)자기가 깨져있는 경우 다음 계란으로
    if eggs[start][0]<=0:
        dfs(start+1)
        return
    check=True
    for i in range(n):
        if i==start:
            continue
        if eggs[i][0] > 0:
            check=False
            break
    #제한사항 2)자기를 제외한, 깰 계란이 없을 경우
    if check:
        #본인빼고 다이니까,
        answer=max(answer,n-1)
        return
    for i in range(n):
        if i==start or eggs[i][0]<=0:
            continue
        eggs[start][0]-=eggs[i][1]
        eggs[i][0]-=eggs[start][1]
        dfs(start+1)
        #다시 원상복귀, 백트래킹
        eggs[start][0]+=eggs[i][1]
        eggs[i][0]+=eggs[start][1]
answer=0
dfs(0)
print(answer)




