text = input("Введите текст: ")
text = text.lower()

punctuation = [".", ",", "!", "?"]

for char in punctuation:
    text = text.replace(char, "")

words = text.split()

word_frequency = {}

for word in words:
    # Подсчет частоты слов
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

print("Количество разных слов:", len(set(words)))

print("Частота слов:")
for word, frequency in word_frequency.items():
    print(f"{word}: {frequency}")
