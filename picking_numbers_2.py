n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
a.sort()
C = []
for i in range(n):
    count = 0
    for j in range(n):
        if(i == j):
            continue
        if(abs(a[j]-a[i])<=1):
            count = count+1

    C.append(count)
print(max(C))