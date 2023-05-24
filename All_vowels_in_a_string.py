s=input()
lst=[]
vowels='aeiou'
for i in vowels:
    if i not in s:
        lst.append(i)
if len(lst)==0: print("True")
else: print("False")