n=int(input())
board=[]
teacher=0
for _ in range(n):
    temp=list(map(str,input().split()))
    teacher+=temp.count('T')    
    board.append(temp)

dx=[-1,1,0,0]
dy=[0,0,-1,1]
def check_S(x,y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        while 0<=nx<n and 0<=ny<n and board[nx][ny]!='O':
            if board[nx][ny]=='S':
                return False
            else:
                nx+=dx[i]
                ny+=dy[i]
    #감시 불가능
    return True
    
def dfs(cnt):
    global answer
    #가지치기
    if cnt==3:
        tt_count=0
        for i in range(n):
            for j in range(n):
                #T입장에서 감시할 학생이 없으면
                if board[i][j]=='T' and check_S(i,j):
                    tt_count+=1
        if tt_count==teacher:
            answer=True
        return
    
    for i in range(n):
        for j in range(n):
            if board[i][j]=='X':
                board[i][j]='O'
                dfs(cnt+1)
                board[i][j]='X'

answer=False
dfs(0)
if answer:
    print('YES')
else:
    print('NO')