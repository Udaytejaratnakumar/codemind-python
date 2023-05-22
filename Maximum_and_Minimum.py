n=int(input())
lst=list(map(int,input().split()))
lst1=list(set(lst))
lst2=[]
flag=0
for i in lst1:
    if i==lst.count(i):
        flag=1
        lst2.append(i)
lst2.sort()
if flag==0: print(-1)
else: print(lst2[0],lst2[len(lst2)-1])
