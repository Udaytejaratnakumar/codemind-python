n=int(input())
lst=list(map(int,input().split()))
lst1=[]
for i in lst:
    if i not in lst1:
        lst1.append(i)
for i in lst1:
    print(i,lst.count(i),sep=' ',end=' ')