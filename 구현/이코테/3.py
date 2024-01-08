n,m=map(int,input().split())
x,y,direction=map(int,input().split())

#방문 처리
d=[[0]*m for _ in range(n)]
d[x][y]=1

array=[list(map(int,input().split())) for _ in range(n)]

#북동남서
dx=[-1,0,1,0]
dy=[0,1,0,-1]

#왼쪽 회전
def turn_left():
    global direction
    direction-=1
    if direction == -1:
        direction=3

#시뮬
cnt=1
turn_time=0
while True:
    turn_left()
    nx=x+dx[direction]
    ny=y+dy[direction]

    #육지이고, 가보지 않은 칸이라면
    if array[nx][ny] ==0 and d[nx][ny] == 0:
        d[nx][ny]=1
        x=nx
        y=ny
        cnt+=1
        turn_time=0
        continue
    else:
        turn_time+=1
    #네방향 모두 갈 수 없는 칸들이라면
    if turn_time==4:
        #뒤로 이동
        nx=x-dx[direction]
        ny=y-dy[direction]
        #가능하다면
        if array[nx][ny] ==0:
            x=nx
            y=ny
        #모두 바다인 경우
        else:
            break
        turn_time=0

print(cnt)



