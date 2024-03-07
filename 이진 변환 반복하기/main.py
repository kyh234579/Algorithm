#십진수를 이진수로 변환
def bit_change(num):
    str_=''
    if num==1:
        return '1'
    while num!=0:
        if num%2 ==0:
            str_='0'+str_
        else:
            str_='1'+str_
        num//=2
    return str_

def solution(s):
    answer = [0,0]
    
    #0제거 -> 제거 후(제거한 0의 개수 count) 길이 계산-> 이진수 변환 (이진 변환 횟수 누적 count)
    while s!='1':
        for char in s:
            if char=='0':
                answer[1]+=1
        s=s.replace('0','')
        s=bit_change(len(s))
        answer[0]+=1
    
    return answer