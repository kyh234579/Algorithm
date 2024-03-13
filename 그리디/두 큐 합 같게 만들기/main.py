from collections import deque
def solution(queue1, queue2):
    answer=-1
    n=len(queue1)
    q1=deque(queue1)
    q2=deque(queue2)
    sum1=sum(queue1)
    sum2=sum(queue2)
    cnt=0
    #두 큐를 합친 길이=2*n, 반복 작업 후 다시 원래 배열로 돌아오는 경우 cnt= 2*2*n 
    while cnt!=n*4:
        if sum1 < sum2:
            tmp=q2.popleft()
            sum1+=tmp
            sum2-=tmp
            q1.append(tmp)
        elif sum1 > sum2:
            tmp=q1.popleft()
            sum2+=tmp
            sum1-=tmp
            q2.append(tmp)
        elif sum1 == sum2:
            answer=cnt
            break
        cnt+=1
            
    return answer