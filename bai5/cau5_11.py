print("Lê Văn Hảo")
print("235752021610027")
import numpy as np

# Tạo mảng có cấu trúc với tên, lớp và chiều cao
data_type = [('name', 'U20'), ('class', 'i4'), ('height', 'f4')]
students = np.array([
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.1),
    ('Pit', 5, 40.11)
], dtype=data_type)

# In mảng ban đầu
print("Mảng ban đầu:")
print(students)

# Sắp xếp theo lớp trước, sau đó theo chiều cao
sorted_students = np.sort(students, order=['class', 'height'])

# In mảng đã sắp xếp
print("\nMảng đã sắp xếp:")
print(sorted_students)
