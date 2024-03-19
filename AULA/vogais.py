def count_words(file_path):
    palindromo = palindromo.replace(" ", ""). lower()
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        palindromo_count = 0
        if palindromo == palindromo [::-1]:
              palindromo_count += 1
        return palindromo_count
    
archive = 'book/download_file.txt'
total_words = count_words(archive)
print(total_words)