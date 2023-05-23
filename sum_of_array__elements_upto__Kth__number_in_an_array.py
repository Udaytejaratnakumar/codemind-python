n=int(input())
lst=list(map(int,input().split()))
k=int(input())
s=0
for i in lst:
    s+=i
    if i==k:
        break
print(s)    