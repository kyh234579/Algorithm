n,m,k=map(int,input().split())
number=list(map(int,input().split()))
number.sort()
num1=number[-1]
num2=number[-2]
#가장 큰 수 더하는 횟수
count=int(m/(k+1)) * k
count+= m%(k+1)

result=0
result+=count*num1
result+=(m-count)*num2

print(result)
