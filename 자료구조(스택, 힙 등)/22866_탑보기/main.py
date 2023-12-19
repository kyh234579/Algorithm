n=int(input())
t_list=list(enumerate(map(int,input().split()),start=1))
count=[0]*(n+1)
nearest=[float("inf")] * (n+1)

def solution(building):
    visibles=[]
    for idx,height in building:
        while visibles and visibles[-1][1] <= height:
            visibles.pop()
        count[idx]+=len(visibles)
        if visibles and abs(visibles[-1][0]-idx) < abs(nearest[idx]-idx):
            nearest[idx] = visibles[-1][0]

        visibles.append((idx,height))

solution(t_list[:])
solution(t_list[::-1])

for i in range(1,n+1):
    if count[i] == 0:
        print(count[i])
    else:
        print(count[i],nearest[i])