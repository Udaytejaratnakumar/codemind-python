n=int(input())
# print(n)
ans=0
for i in range(len(str(n))):
     ans+=int(str(n)[i])**(i+1)
if n==ans: print("True")
else: print("False")