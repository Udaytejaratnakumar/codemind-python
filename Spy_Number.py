n=int(input())
lst=[]
while(n):
    lst.append(n%10)
    n//=10
s=0;p=1
for i in lst:
    s+=i
    p*=i
if(s==p): print("Spy Number")
else: print("Not Spy Number")