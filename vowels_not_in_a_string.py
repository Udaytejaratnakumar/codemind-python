s=input()
vowels='aeiou'
flag=0
for i in vowels:
    if i not in s:
        flag=1
        print(i,end=' ')
if flag==0: print(0)