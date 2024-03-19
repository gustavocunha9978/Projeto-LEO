def is_palindrome(word):
    word = word.replace(" ", "").lower()
    return word == word[::-1]


def count_words(file_path):
    palindrome_count = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        words = content.split()
        for word in words:
            if is_palindrome(word):
                palindrome_count += 1
        return palindrome_count


archive = 'book/download_file.txt'
total_words = count_words(archive)
print(total_words)
