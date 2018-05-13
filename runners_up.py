n = int(input())
A = [int(x) for x in input().split(' ')]

B = [x for x in A if x!=max(A)]
print(max(B))