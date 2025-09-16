sentence = input("Enter a sentence: ")
words = sentence.split()

longest_word = ""
max_length = 0

for word in words:
    if len(word) > max_length:
        max_length = len(word)
        longest_word = word

print("Longest word:", longest_word)
print("Length:", max_length)
