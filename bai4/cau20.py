print("SV: Le Van Hao")
print("MSSV: 235752021610027")
def pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = [1]
        if triangle:
            last_row = triangle [-1]
            row.extend((last_row (j) + last_row [j + 1] for j
            row.append(1)
        triangle.append (row)
    return triangle
n = int(input(" Nhập số dòng n: "))
triangle pascal_triangle (n)
for row in triangle:
print(row) 
