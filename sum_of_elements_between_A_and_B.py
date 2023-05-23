n=int(input())
lst=list(map(int,input().split()))
a,b=map(int,input().split())
s=0
for i in lst:
    if i>=a and i<=b:
        s+=i
print(s)