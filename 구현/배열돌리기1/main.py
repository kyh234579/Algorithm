n,m,r=map(int,input().split())
board=[]
for _ in range(n):
    temp=list(map(int,input().split()))
    board.append(temp)

for _ in range(r):
    #제일바깥부터 차례로 원형 순환
    for i in range(min(n,m)//2):
        #첫 시작 인덱스
        x,y=i,i
        #첫값 저장.
        value=board[x][y]
        #좌측
        for j in range(i+1,n-i):
            x=j
            #현재값 저장
            temp=board[x][y]
            #이전값 대입
            board[x][y]=value
            #현재값을 다시 이전값으로 갱신
            value=temp
        #하단
        for j in range(i+1,m-i):
            y=j
            temp=board[x][y]
            board[x][y]=value
            value=temp
        #우측
        for j in range(i+1,n-i):
            x=n-1-j
            temp=board[x][y]
            board[x][y]=value
            value=temp
        #상단
        for j in range(i+1,m-i):
            y=m-1-j
            temp=board[x][y]
            board[x][y]=value
            value=temp          

for i in range(n):
    for j in range(m):
        print(board[i][j],end=' ')
    print()