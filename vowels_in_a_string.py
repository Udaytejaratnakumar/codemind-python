s=input()
o=input()
flag=0
for i in range(len(s)):
    if o==s[i]: 
        flag=1
        print('True',i,sep='
')
        break
if flag==0: print("False")