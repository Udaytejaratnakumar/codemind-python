n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
flag=0
if (arr[0]==a and arr[len(arr)-1]==b):
    print(-1)
else:
    m=0
    for i in arr:
        if i<a or i>b:
            flag=1
            if i>m:
                m=i
if(flag==0): print(-1)
else:print(m)
