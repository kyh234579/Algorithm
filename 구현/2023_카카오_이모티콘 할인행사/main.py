def solution(users, emoticons):
    data=[10,20,30,40]
    answer = [0,0]
    discount=[]
    #dfs로 할인률의 모든 경우의 수 만들기 -> discount=[]
    def dfs(temp,depth):
        if depth==len(emoticons):
            discount.append(temp[:])
            return
        for d in data:
            temp[depth]+=d
            dfs(temp,depth+1)
            #백트래킹?
            temp[depth]-=d
    
    dfs([0]*len(emoticons),0)
    
    for d in range(len(discount)):
        plus_signer=0
        profit=0
        for user in users:
            buy_sum=0    
            for j in range(len(discount[d])):
                if user[0] <= discount[d][j]:
                    buy_sum+=emoticons[j]*(1-(discount[d][j]/100))
            if user[1] <= buy_sum:
                plus_signer+=1
            else:
                profit+=buy_sum
        if answer[0] < plus_signer:
            answer=[plus_signer,int(profit)]
        elif answer[0] == plus_signer and answer[1]<int(profit):
            answer=[plus_signer,int(profit)]
            
    
    return answer