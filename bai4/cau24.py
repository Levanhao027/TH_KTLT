def count_upper_lower(input_str):
    upper_count = 0
    lower_count = 0
    for char in sentence:
        if char.isupper():
          # Kiểm tra xem ký tự có phải là chữ hoa không
            upper_count += 1
        elif char.islower():
          # Kiểm tra xem ký tự có phải là chữ thường không
            lower_count += 1
    return upper_count, lower_count  
# Nhập câu
input_sentence = input("Nhập một câu: ")
upper_letters, lower_letters = count_upper_lower(input_sentence)
# In kết quả
print("Số chữ hoalà:", upper_letters)
print("Số chữ thường là:", lower_letters)
