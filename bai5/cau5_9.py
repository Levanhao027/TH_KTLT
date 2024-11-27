 
# main.py
from search_module import binary_search
# Nhập số lượng phần tử trong danh sách
n=int(input("Enter the number of elements in the list: "))
# Nhập các giá trị vào danh sách
1st = []
for i in range (n):
    value = int(input(f"Enter the {i + 1}th element: "))
    lst.append(value)
# Sắp xếp danh sách trước khi tìm kiếm
lst.sort()

# Nhập phần tử cần tìm
value = int(input("Nhập phần tử cần tìm: "))

# Tìm kiếm phần tử

found = binary_search (lst, value)
# In kết quả
if found:
   print (f"Phần tử (value) có trong danh sách.")
else:
   print (f"Phần tử {value} không có trong danh sách.")
