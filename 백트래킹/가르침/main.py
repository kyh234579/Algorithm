n,k=map(int,input().split())
words=[]
visited=[0]*26
for _ in range(n):
    words.append(set(input().rstrip()))
for c in ['a','n','t','i','c']:
    visited[ord(c)-ord('a')]=1
answer=0
def dfs(start,cnt):
    global answer
    #가지치기, 인덱스가 넘어가면 갯수 저장.
    if cnt==k-5:
        tmp=0
        for word in words:
            #배운 글자로 해당 글자 읽을 수 있는지 확인
            is_check=True
            for char in word:
                if not visited[ord(char)-ord('a')]:
                    is_check=False
                    break
            #읽을 수 있으면 갯수세기
            if is_check:
                tmp+=1
        answer=max(answer,tmp)
        return
    
    for i in range(start,26):
        if not visited[i]:
            visited[i]=1
            dfs(i,cnt+1)
            visited[i]=0

if k<5:
    print(0)
    exit(0)
elif k==26:
    print(n)
    exit(0)

dfs(0,0)
print(answer)
        