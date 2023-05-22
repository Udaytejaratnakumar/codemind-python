n=int(input())
lst=list(map(int,input().split()))
c,s=0,0
flag=0
lst1=list(set(lst))
for i in lst1:
    if i==lst.count(i):
        flag=1
        c+=1
        s+=i
if flag==0: print(-1)
else: print("%.2f"%(s/c))