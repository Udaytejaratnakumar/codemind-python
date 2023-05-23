n=int(input())
lst=list(map(int,input().split()))
i=0
j=len(lst)-1
while(i<j):
    print(lst[i],lst[j],sep=' ',end=' ')
    i+=1
    j-=1
if i==j:
    print(lst[i],0)