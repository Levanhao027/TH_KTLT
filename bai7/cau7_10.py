print("Le Van Hao")
print("235752021610027")
def find_longest_words (text):
    # Tách văn bản thành các từ
    words = text.split()

    # Tìm độ dài của từ dài nhất
    max_length = max(len (word) for word in words)

    # Lọc ra các từ có độ dài bằng với từ dài nhất
    longest_words = [word for word in words if len (word) == max_length]
    return longest_words

text = "kỹ thuật lập trình"
longest words find longest words (text)
print("Những từ dài nhất:", longest_words)
