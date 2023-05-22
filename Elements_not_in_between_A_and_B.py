n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
flag=0
for i in arr:
    if i<a or i>b:
        flag=1
        print(i,end=' ')
if flag==0: print(-1)