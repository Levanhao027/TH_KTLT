chuoi = input("Nhap mot chuoi: ")
chuoi_moi = ''.join([ky_tu for ky_tu in chuoi if not ky_tu.isdigit()])
print("Chuoi moi: ",chuoi_moi)