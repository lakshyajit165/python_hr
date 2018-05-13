A = input()
B = []
for i in range(len(A)):
    if(A[i].isalpha()):
        if(A[i].isupper()):
            B.append(A[i].lower())
        elif(A[i].islower()):
            B.append(A[i].upper())
    else:
        B.append(A[i])
for i in B:
    print(i,end='')