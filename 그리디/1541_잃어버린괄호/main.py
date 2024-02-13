#'+'를 먼저 연산 후에 '-' 연산
#1.'-'를 기준으로 나누기
exp=input().split('-')
num=[]
for i in exp:
    sum=0
    #2.'+'를 기준으로 나누기
    tmp=i.split('+')
    for j in tmp:
        sum+=int(j)
    num.append(sum)
n=num[0]
for i in range(1,len(num)):
    n-=num[i]
print(n)