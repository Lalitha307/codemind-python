a=int(input())
for i in range(a):
    for j in range(1,a-1):
        print(j,end="")
    for j in range(1,a-2):
        print(j,end="")
    print()