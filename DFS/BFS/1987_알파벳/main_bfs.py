r, c = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    q=set()
    q.add((0,0,board[0][0]))
    result=1
    while q:
        x,y,visited=q.pop()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=r or ny>=c:
                continue
            elif board[nx][ny] not in visited:
                next_visited=visited+board[nx][ny]
                q.add((nx,ny,next_visited))
                result=max(result,len(next_visited))
    
    return result

print(bfs())
