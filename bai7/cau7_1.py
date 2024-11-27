tạo 1 file a.txt lưu vào ổ đĩa D
print("Lê Văn Hảo")
print("235752021610027")
input_file=open('D:/a.txt','r')
for line in input_file:
    l=len (line)
    s=''
    while (l>=1):
        s=s+line [l-1]
        l=l-1
print (s)
input_file.close()
