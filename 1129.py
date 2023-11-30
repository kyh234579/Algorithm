def solution(n, times):
    answer = 0
    left=min(times)
    right=max(times)*n
    
    while left <= right :
        mid = (left+right) //2
        res=0
        for time in times:
            res+=mid//time
            if res >= n:
                break
        if res >=n:
            answer=mid
            right=mid-1
        else:
            left=mid+1
        
    return answer