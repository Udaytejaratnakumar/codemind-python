s=input()
s=s.split(' ')
m=len(s[0])
for i in s:
    if m>len(i): m=len(i)
print(m)