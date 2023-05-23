n=int(input())
lst=list(map(int,input().split()))
ls=[i for i in lst if i%2==0]
ls=set(ls)
print(sum(ls))