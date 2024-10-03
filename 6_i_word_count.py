from collections import Counter

text = "Data science is a fascinating field, and learning Python makes it even more exciting. Python is powerful."
word_list = text.lower().split()
word_freq = Counter(word_list)


print(text)
word = input("Enter a word to find its frequency: ").lower()
print("Frequency of 'python':", word_freq[word])
