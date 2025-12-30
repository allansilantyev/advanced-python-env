text = input("Enter a string: ")

words = text.split()  # разделяем строку на слова
sorted_words = [''.join(sorted(word)) for word in words]  # сортируем буквы в каждом слове

result = ' '.join(sorted_words)
print("Sorted string:", result)
