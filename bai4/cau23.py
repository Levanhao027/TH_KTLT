def count_letters_and_digits(input_str):
    letter_count = 0
    digit_count = 0
    
    for char in sentence:
        if char.isalpha():
          # Kiểm tra xem ký tự có phải là chữ cái không
            letter_count += 1
        elif char.isdigit():
          # Kiểm tra xem ký tự có phải là chữ số không
            digit_count += 1
    return letter_count, digit_count
# Nhập vào câu từ người dùng
input_sentence = input("Nhập một câu: ")
letters, digits = count_letters_and_digits(input_sentence)
# In kết quả
print("Số chữ cái là:", letters )
print("Số chữ số là":", digits)
