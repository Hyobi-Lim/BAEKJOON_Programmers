import sys
student=set([i for i in range(1,31)])
submitted_student=set()
for i in range(28):
    submitted_student.add(int(sys.stdin.readline()))
print(min(student-submitted_student))
print(max(student-submitted_student))