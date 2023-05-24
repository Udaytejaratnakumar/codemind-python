def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2: return True
    else: return False
n=int(input())
lst=list(map(int,input().split()))
lst1=[i for i in lst if prime(i)]
print("%.2f"%(sum(lst1)/len(lst1)))