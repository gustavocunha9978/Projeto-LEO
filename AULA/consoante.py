def count_words(file_path):
    vowels = 'aeiouAEIOU'
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        consonant_count = 0
        for char in content:
          if char.isalpha() and char not in vowels:
              consonant_count += 1
        return consonant_count
    
archive = 'book/download_file.txt'
total_words = count_words(archive)
print(total_words)