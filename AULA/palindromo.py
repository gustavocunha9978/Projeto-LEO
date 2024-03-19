def count_words(file_path):
    vowels = 'aeiouAEIOU'
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        vowels_count = 0
        for char in content:
          if char in vowels:
              vowels_count += 1
        return vowels_count
    
archive = 'book/download_file.txt'
total_words = count_words(archive)
print(total_words)