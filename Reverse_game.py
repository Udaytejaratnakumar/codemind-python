n=int(input())
lst=list(map(int,input().split()))
x=lambda n:str(n)[::-1]
lst1=[]
for i in lst:
    lst1.append(int(x(i)))
print(*lst1)