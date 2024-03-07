def solution(friends, gifts):
    n=len(friends)
    #다음달에 받을 선물리스트
    answer = [0]*n
    #주고 받은 선물리스트
    give_list=[[0]*n for _ in range(n)]
    gisu=[[0,0] for _ in range(n)]
    for gift in gifts:
        giver,given=gift.split()
        give_list[friends.index(giver)][friends.index(given)]+=1
    for i in range(n):
        giver_sum=sum(give_list[i])
        gisu[i][0]=giver_sum
    for i in range(n):
        for j in range(n):
            gisu[i][1]+=give_list[j][i]
    #선물 지수
    new_gisu=[]
    for a,b in gisu:
        new_gisu.append(a-b)
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            if give_list[i][j] > give_list[j][i]:
                answer[i]+=1
            if give_list[i][j] == give_list[j][i] and new_gisu[i] > new_gisu[j]:
                answer[i]+=1
    
    return max(answer)