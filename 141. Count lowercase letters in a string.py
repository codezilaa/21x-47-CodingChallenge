input_str = input("Enter the string")
count = 0
for char in input_str:
    if char.islower():
        count = count+1
        print(count)