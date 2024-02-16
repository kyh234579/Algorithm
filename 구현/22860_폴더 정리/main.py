import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n,m=map(int,input().split())
dict={}

def find_files(path,array):
    if path not in dict.keys():
        return
    for f in dict[path]:
        if f[1]==0:
            array.append(f[0])
        else:
            find_files(f[0],array)

for _ in range(n+m):
    parent,child,is_folder=input().rstrip().split()
    if parent not in dict.keys():
        dict[parent]=[]
    dict[parent].append([child,int(is_folder)])

query=int(input())
for _ in range(query):
    path=list(input().rstrip().split('/'))
    #file담는 리스트
    files=[]
    find_files(path[-1],files)
    print(len(list(set(files))),len(files))