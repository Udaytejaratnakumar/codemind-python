n=int(input())
lst=list(map(int,input().split()))
x=(lambda n:str(n)==str(n)[::-1])
c=0
for i in lst:
    if x(i):c+=1
print(c)