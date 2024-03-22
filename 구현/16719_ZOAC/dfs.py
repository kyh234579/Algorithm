word=list(input().rstrip())
n=len(word)
answer=['']*n

#s,start 현재배열,시작지점 인덱스
def dfs(s,start):
    global answer

    if not s:
        return

    #현재 배열의 최소값, 그것의 인덱스
    target=min(s)
    idx=s.index(target)

    answer[start+idx]=target
    print(''.join(answer))

    #뒷배열 먼저 순회
    dfs(s[idx+1:],start+idx+1)
    dfs(s[:idx],start)


dfs(word,0)