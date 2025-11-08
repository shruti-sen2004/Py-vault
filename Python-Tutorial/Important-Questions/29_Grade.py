def age_greater_20(m):
    for i in range(len(m)):
        if int(m[i][1]) > 20:
            print(m[i][0]) 

def avg_marks_fem(m):
    marks = 0
    total = 0
    for i in range(len(m)):
        if m[i][-1] == 'Female':
            marks += ord(m[i][2])
            total += 1
    print(marks/total)


n = int(input())
# arr = [['Alice', '22', 'A', 'Female'], ['Bob', '19', 'B', 'Male'], ['Carol', '21', 'B', 'Female'], ['David', '23', 'C', 'Male'], ['Eve', '20', 'A', 'Female']]
arr =[]

for i in range(n):
    inp = input().split()
    arr.append(inp)
age_greater_20(arr)
avg_marks_fem(arr)