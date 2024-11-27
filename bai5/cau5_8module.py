print("SV: Lê Văn Hảo")
print("MSSV: 235752021610027")
 # search_module.py
def sequential_search(dlist, item):
    """Tìm kiếm tuyến tính trong danh sách."""
    for index in range(len(dlist)):
        if dlist[index] == item:
            return index 
    return -1 
