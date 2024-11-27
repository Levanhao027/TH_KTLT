# main.py

from search_module import sequential_search

# Nhập số lượng phần tử trong danh sách
n = int(input("Nhập số lượng phần tử trong danh sách: "))

# Nhập các giá trị vào danh sách
dlist = []
for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i + 1}: "))
    dlist.append(value)

# Nhập phần tử cần tìm
item = int(input("Nhập phần tử cần tìm: "))

# Tìm kiếm phần tử
result_index = sequential_search(dlist, item)

# In kết quả
if result_index != -1:
    print(f"Phần tử {item} được tìm thấy tại chỉ số: {result_index}")
else:
    print(f"Phần tử {item} không có trong danh sách.")
