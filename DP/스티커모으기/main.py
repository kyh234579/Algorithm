def solution(sticker):
    answer = 0
    n=len(sticker)
    if n==1:
        return sticker[0]
    #1번째 스티커를 고를 경우, 고르지 않을 경우
    table=[[0]*n for _ in range(2)]
    table[0][0]=sticker[0]
    table[0][1]=sticker[0]
    table[1][1]=sticker[1]
    #첫번째 경우
    for i in range(2,n-1):
        #해당(i번째) 스티커를 고르지 않는 경우, 고르는 경우 
        table[0][i]=max(table[0][i-1],sticker[i]+table[0][i-2])
    #두번째 경우
    for i in range(2,n):
        #해당(i번째) 스티커를 고르지 않는 경우, 고르는 경우 
        table[1][i]=max(table[1][i-1],sticker[i]+table[1][i-2])
    answer=max(table[0][n-2],table[1][n-1])


    return answer