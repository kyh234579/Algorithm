def solution(cap, n, deliveries, pickups):
    answer = 0
    #현재 배달 가능한, 배달 잔여 갯수
    deliver=0
    #현재 수거 가능한, 수거 잔여 갯수
    pick=0
    for i in range(n-1,-1,-1):
        #해당 집으로 다시 와야하는 횟수
        cnt=0
        #해당 집의 배달/수거 갯수 둘 중에 하나라도, 잔여 갯수보다 클 경우 다시 와야함. 
        while deliver<deliveries[i] or pick<pickups[i]:
            cnt+=1
            deliver+=cap
            pick+=cap
        deliver-=deliveries[i]
        pick-=pickups[i]
        answer+=(i+1)*cnt
    
    return 2*answer