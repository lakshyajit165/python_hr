marksheet = [[input(), float(input())] for _ in range(int(input()))]
A = []

for i in range(len(marksheet)):
    A.append(marksheet[i][1])

B = [x for x in A if x!=min(A)]

C = []
for i in range(len(marksheet)):
    if(marksheet[i][1] == min(B)):
        C.append(marksheet[i][0])
C.sort()
for i in C:
    print(i)