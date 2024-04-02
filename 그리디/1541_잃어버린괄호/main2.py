#뺄셈을 나중에 연산하기 위해서
#덧셈연산을 모두 한 뒤, 리스트에 담고, 앞에서부터 차례대로 빼주기
s=input().split('-')
lst=[]
for num in s:
    sum=0
    tmp=num.split('+')
    for j in tmp:
        sum+=int(j)
    #더한값 리스트에 담기
    lst.append(sum)
result=lst[0]
for i in range(1,len(lst)):
    result-=lst[i]
print(result)
