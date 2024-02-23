n=int(input())
calender=[0]*366

for _ in range(n):
    s,e=map(int,input().split())
    for i in range(s,e+1):
        calender[i]+=1

result=0
row=0
col=0
for day in calender:
    #일정이 있을때
    if day!=0:
        row+=1
        col=max(col,day)
    #일정이 없을때
    else:
        result+=row*col
        row=0
        col=0
#나머지 일정이 있는 상태에서 끝날수 있으므로, 나머지 일정도 더해주기
result+=row*col

print(result)

