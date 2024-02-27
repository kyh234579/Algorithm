n=int(input())
#1,2,3으로 이뤄진 좋은 수열 중 가장 작은 수 출력
def dfs(result,cnt):
    #제한사항1) 나쁜 수열이면 return
    for i in range(1,cnt//2+1):
        if str(result)[cnt-i:]==str(result)[cnt-2*i:cnt-i]:
            return       
    #가지치기
    if cnt==n:
        print(result)
        exit(0)    
        return
    for i in range(1,4):
        temp=result*10 + i
        dfs(temp,cnt+1)

dfs(0,0)
