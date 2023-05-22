n=int(input())
lst=list(map(int,input().split()))
lst1=list(set(lst))
c=0
for i in lst1:
    if i==lst.count(i):
        c+=1
print(c)