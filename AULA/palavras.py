def count_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        words = content.split()
        return len(words)

archive = 'book/download_file.txt'
total_words = count_words(archive)
print(total_words)
