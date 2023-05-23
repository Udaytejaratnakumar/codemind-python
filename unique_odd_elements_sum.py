n=int(input())
lst=list(map(int,input().split()))
lt=[i for i in lst if i%2==1]
lt=set(lt)
print(sum(lt))