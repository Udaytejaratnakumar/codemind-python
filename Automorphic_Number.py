n=int(input())
a=n*n
a=str(a)
b=str(n)
if a.endswith(b): print("Automorphic Number")
else: print("Not an Automorphic Number")