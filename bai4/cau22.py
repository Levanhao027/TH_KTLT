print("SV: Le Van Hao")
print("MSSV: 235752021610027")
def is_all_even_digits (num):
    return all(int (digit)2 for digit in str(num))
def find_even_digit_numbers (start, end):
    even_digit_numbers - []
    for num in range (start, end + 1):
        if is_all_even_digits (num):
            even_digit_numbers.append(num)
    return even digit_numbers
start = 1000
end = 3000
result find_even_digit_numbers (start, end) 
print("Các số có tất cả chữ số là số chẵn trong đoạn từ 1000 đến 3000 là:",', '.join(map(str, result)))
