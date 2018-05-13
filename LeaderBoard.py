n = int(input())
A = [int(x) for x in input().split()]
m = int(input())
B = [int(x) for x in input().split()]
S = set(A)
C = []
for i in S:
    C.append(i)

for i in B:
    C.append(i)
    C.sort()
    C.reverse()
    print(C.index(i)+1)
    C.remove(i)

