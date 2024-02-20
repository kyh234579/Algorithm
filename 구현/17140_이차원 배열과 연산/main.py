from collections import Counter
r,c,k=map(int,input().split())
#초기 리스트 
A=[]
for _ in range(3):
    temp=list(map(int,input().split()))
    A.append(temp)

def sorted_new(array,RC):
    #정렬된 배열 결과
    sorted_arr=[]
    max_cnt=0
    for i in range(len(array)):
        counter=Counter(array[i])
        B=[]
        for key,value in counter.items():
            if key==0:
                continue
            B.append([key,value])
        B.sort(key=lambda x:[x[1],x[0]])
        #2차원 배열을 1차원 배열로 변환 []+[]=[]
        C=sum(B,[])
        sorted_arr.append(C)
        max_cnt=max(max_cnt,len(C))
    #제일 열이 긴 행 기준으로 나머지 0으로 채우기
    for i in sorted_arr:
        i+=[0]*(max_cnt-len(i))
        #길이가 100이 넘어가는 경우, 나머지 버리기
        if len(i)>100:
            i=i[:100]
    if RC=='R':
        return sorted_arr
    else:
        return list(zip(*sorted_arr))
time=0
while True:
    if time>100:
        time=-1
        break
    if r-1<len(A) and c-1<len(A[0]):
        if A[r-1][c-1]==k:
            break
    if len(A)>=len(A[0]):
        A=sorted_new(A,'R')
    else:
        A=sorted_new(list(zip(*A)),'C')
    time+=1
print(time)
            
