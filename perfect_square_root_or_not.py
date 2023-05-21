n=int(input())
for i in range(n//2):
    if i*i==n: 
        print('True')
        break
    elif i*i>n: 
        print("False")
        break