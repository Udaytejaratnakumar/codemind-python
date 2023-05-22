n=int(input())
lst=list(map(int,input().split()))
k=int(input())
lst1=list(set(lst))
flag=0
for i in lst1:
    if lst.count(i)==k:
        flag=1
        print(i,end=' ')
if flag==0: print(-1)