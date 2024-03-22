def count_vowels(file_path):
    vowels = 'aeiouAEIOU'
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        vowel_count = 0
        for char in content:
            if char in vowels:
                vowel_count += 1
        return vowel_count

archive = 'book/download_file.txt'
total_vowels = count_vowels(archive)
print("Total de vogais:", total_vowels)
