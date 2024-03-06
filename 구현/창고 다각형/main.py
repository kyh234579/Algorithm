n=int(input())
#최대값
m=0
#최대값 인덱스
m_idx=0
#인덱스마다 기둥 높이
pils=[0]*1001
for _ in range(n):
    L,H=map(int,input().split())
    pils[L]=H
    if m < H:
        m_idx=L
        m=H
    
answer=0
curr=0
#왼쪽그룹, (최대 높이 기둥을 포함한)
for i in range(m_idx+1):
    curr=max(curr,pils[i])
    answer+=curr
curr=0
#오른쪽그룹, 내림차순
for i in range(1000,m_idx,-1):
    curr=max(curr,pils[i])
    answer+=curr

print(answer)




