sentence = input("Enter a sentence: ")
words = sentence.split()


shortest_word = ""
min_length = 1

for word in words:
    if len(word) < min_length:
        min_length = len(word)
        longest_word = word

print("short word:", shortest_word)
print("Length:", min_length)