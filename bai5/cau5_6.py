 lưu ý lưu vơi tên main.py
# main.py
từ mymodule nhập sort_list, find_maximum, find_minimum

# Nhập số lượng phần tử trong danh sách
n = int(input("Nhập số lượng phần tử trong danh sách: "))

# Nhập các giá trị vào danh sách
input_list = []
for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i + 1}: "))
    input_list.append(value)

# Sắp xếp danh sách
sorted_list = sort_list(input_list)

# Tìm phần tử lớn nhất và nhỏ nhất
max_value = find_maximum (sorted_list)
min_value = find_minimum (sorted_list)

# In kết quả
print("Danh sách đã sắp xếp:", sorted_list)
print("Phần tử lớn nhất là:", max_value)
print("Phần tử nhỏ nhất là:", min_value)
