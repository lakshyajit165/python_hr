n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

A = list(student_marks[query_name])
avg = sum(A)/float(len(A))
print("{:.2f}".format(avg))
