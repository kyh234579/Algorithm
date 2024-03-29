#I, V, X, L, C, D, M
word_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
value_sort=sorted(word_dict.items(),key=lambda x:x[1],reverse=True)

total=0
for _ in range(2):
    str=input().rstrip()
    result=0
    i=0
    while i < len(str):
        if i < len(str)-1 and str[i:i+2] in word_dict.keys():
            result+=word_dict[str[i:i+2]]
            i+=2
        else:
            result+=word_dict[str[i]]
            i+=1
    total+=result
print(total)

result_str=''
for key,value in value_sort:
    if total ==0:
        break
    cnt=total//value
    total=total%value
    result_str+=key*cnt


print(result_str)