n=int(input())
s=input()
cnt=[]

#좌측으로 R 모으기
l_Rexplore=s.lstrip('R')
cnt.append(l_Rexplore.count('R'))

#좌측으로 B 모으기
l_Bexplore=s.lstrip('B')
cnt.append(l_Bexplore.count('B'))

#우측으로 R 모으기
r_Rexplore=s.rstrip('R')
cnt.append(r_Rexplore.count('R'))

#우측으로 B 모으기
r_Bexplore=s.rstrip('B')
cnt.append(r_Bexplore.count('B'))

print(min(cnt))