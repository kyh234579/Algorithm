n=int(input())
now=list(map(int,input().rstrip('\n')))
target=list(map(int,input().rstrip('\n')))

def change(light,target):
    #스위치 누른 갯수 세기
    cnt=0
    for i in range(1,n):
        if light[i-1]==target[i-1]:
            continue
        cnt+=1
        for j in range(i-1,i+2):
            if j<n: 
                light[j]=1-light[j]
    #이렇게 해서, target과 일치가 되면(성공하면)
    if light==target:
        return cnt
    else:
        return 1e9

#첫번째 스위치를 누르지 않은 경우
case0=change(now[:],target)
#첫번째 스위치를 누른 경우
now[0]=1-now[0]
now[1]=1-now[1]
case1=change(now[:],target)+1

result=min(case0,case1)

if result==1e9:
    print(-1)
else:
    print(result)