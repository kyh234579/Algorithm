import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
#폴더 갯수, 파일 갯수
n,m=map(int,input().split())
dict={}

def find_files(path,array):
    if path not in dict:
        return
    for f in dict[path]:
        #파일이라면
        if f[1]==0:
            array.append(f[0])
        else:
            find_files(f[0],array)

for _ in range(n+m):
    root,child,isfolder=input().rstrip().split()
    if root not in dict:
        dict[root]=[]
    dict[root].append([child,int(isfolder)])

query=int(input())
for _ in range(query):
    path=input().rstrip().split('/')
    #파일 담는 리스트
    files=[]
    find_files(path[-1],files)
    print(len(list(set(files))),len(files))