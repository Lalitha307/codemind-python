n=input()

n=n[::-1]

n=n.split(" ")
for i in range(len(n)-1,-1,-1):
    print(n[i],end=" ")