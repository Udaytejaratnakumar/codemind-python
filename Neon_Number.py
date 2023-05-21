n=int(input())
add=0
s=n*n
while(s):
    add=add+(s%10)
    s//=10
if(add==n): print("Neon Number")
else: print("Not Neon Number")
