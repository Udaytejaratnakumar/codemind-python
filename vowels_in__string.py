s=input()
lst=[]
for i in s:
    if i in 'aeiouAEIOU' and i not in lst: lst.append(i)
if len(lst)==0:print(-1)
else: print(*lst)