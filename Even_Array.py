n=int(input())
lst=list(map(int,input().split()))
flag=0
for i in lst:
    if i%2!=0:
        flag=1
        break
if flag==0: print("True")
else: print("False")