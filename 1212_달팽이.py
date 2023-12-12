A,B,V = map(int,input().split())
sum=0
cnt=0
while True:
    sum+=(A-B)
    if sum >= V:
        break
    cnt+=1

print(cnt)