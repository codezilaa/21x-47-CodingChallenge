input_str = input("Enter the string: ")
max_char = ""
max_count=0
for char in input_str:
    count = input_str.count(char)
    if count > max_count:
        max_count = count
        max_char = char
        print(char)
        print(count)