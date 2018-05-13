b,n,m = input().strip().split(' ')
b,n,m = [int(b),int(n),int(m)]
keyboards = [int(x) for x in input().split()]
drives = [int(x) for x in input().split()]

A = []
for i in keyboards:
    for j in drives:
        if((i+j)<=b):
            A.append(i+j)
if(len(A) == 0):
    print(-1)
else:
    print(max(A))
