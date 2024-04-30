n=int(input())
aList=[]
dp=[0]*n
for _ in range(n):
    a,b=map(int,input().split())
    aList.append([a,b])