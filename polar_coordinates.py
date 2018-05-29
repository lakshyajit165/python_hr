import cmath
xx = input()
if('+' in xx):
    c = xx.split('+')

    a = int(c[0])
    b = int(c[1].split('j')[0])
else:
    c = xx.split('-')

    if (xx[0] == '-'):

        a = 0 - int(c[1])
        b = 0 - int(c[2].split('j')[0])
    else:

        a = int(c[0])
        b = 0 - int(c[1].split('j')[0])
print(abs(complex(a,b)))
print(cmath.phase(complex(a,b)))
