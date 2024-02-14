n=int(input())
like_info=[]
seat=[[0]*(n) for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

for _ in range(n*n):
    temp=list(map(int,input().split()))
    now_student=temp[0]
    like_student=temp[1:]
    like_info.append(temp)
    #후보군
    result=[]
    for i in range(n):
        for j in range(n):
            if seat[i][j]==0:
                like_student_cnt=0
                empty_cnt=0
                for k in range(4):
                    nx=i+dx[k]
                    ny=j+dy[k]
                    if nx<0 or nx>=n or ny <0 or ny>=n:
                        continue
                    if seat[nx][ny] in like_student:
                        like_student_cnt+=1
                    if seat[nx][ny]==0:
                        empty_cnt+=1
                result.append((like_student_cnt,empty_cnt,i,j))
    #좋아하는 학생수와 비어있는 칸의 개수는 내림차순, 인덱스는 오름차순
    result=sorted(result,key=lambda x: (-x[0],-x[1],x[2],x[3]))
    seat[result[0][2]][result[0][3]]=now_student
like_info.sort()

#선호도 체크
sum=0
for i in range(n):
    for j in range(n):
        cnt=0
        for k in range(4):
            nx=i+dx[k]
            ny=j+dy[k]
            if nx<0 or nx>=n or ny <0 or ny>=n:
                continue
            if seat[nx][ny] in like_info[seat[i][j]-1]:
                cnt+=1
        if cnt!=0:
            sum+=10**(cnt-1)
print(sum)