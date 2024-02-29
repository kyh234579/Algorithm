n=int(input())
number=[]
#줄어드는 수 리스트, 모두 저장
result=set()
def dfs():
    if number:
        #줄어드는 수 저장.
        result.add(int(''.join(map(str,number))))
    #0~9으로 시작하는~
    for i in range(10):
        #ex) i=2 -> i=0 끝나면 0 pop
        #        -> i=1 -> i=0 끝나면 다시 역순으로 pop
        if not number or number[-1] >i:
            number.append(i)
            dfs()
            #백트래킹
            number.pop() 
dfs()
#집합함수라 sorted으로 ,오름차순 정렬+리스트 변환 만들어놓기
result=sorted(result)
if len(result)<n:
    print(-1)
else:
    print(result[n-1])
    
        