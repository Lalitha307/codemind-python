n=int(input())
while n:
    a=input()
    c=0
    for i in range(len(a)-1):
        if a[i]==a[i+1]:
            c+=1
    print(c)
    n-=1