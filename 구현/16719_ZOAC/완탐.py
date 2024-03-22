word=input()
n=len(word)
isActivate=[0]*n

#활성화시킨 단어 잇기
def showIsActivate(word,isActivate):
    result=''
    for i in range(n):
        if isActivate[i]:
            result+=word[i]
    return result

while True:
    if sum(isActivate)==n:
        break
    temp=[]
    for j in range(n):
        if not isActivate[j]:
            isActivate[j]=1
            #활성화 시켜 이은 단어랑 index 함께 temp에 담기
            temp.append((showIsActivate(word,isActivate),j))
            isActivate[j]=0
    #오름차순 정렬하면 담은 단어중에 사전순으로 가장 이른 단어가 맨 앞에 옴
    temp.sort()
    print(temp[0][0])
    #반환 후, 활성화 체크
    isActivate[temp[0][1]]=1

    