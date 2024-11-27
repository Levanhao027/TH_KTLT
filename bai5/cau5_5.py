lưu ý lưu file với tên main.py
# main.py

from bubble_sort import bubbleSort

# Nhập n phần tử từ bàn phím
input_list = input("Nhập danh sách các số (cách nhau bởi dấu phẩy): ")
nlist = [int(x) for x in input_list.split(",")]

# Sắp xếp danh sách
sorted_list = bubbleSort(nlist)

# In kết quả
print("Danh sách đã sắp xếp:", sorted_list)
