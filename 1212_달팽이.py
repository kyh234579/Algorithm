import math
A,B,V = map(int,input().split())
# a* day - b*(day-1) >= V 이 식을 이항한 것.
day=(V-B)/(A-B)
print(math.ceil(day))