t=int(input())

for _ in range(t):
    n,m=map(int,input().split())
    data=list(map(int,input().split()))
    cnt=0
    while data:
        if data[0]<max(data):
            data.append(data.pop(0))
        else:
            data.pop(0)
            cnt+=1
            if m==0:
                print(cnt)
                break
        if m==0:
            m=len(data)-1
        else:
            m-=1
