input_str = input("Enter the string: ")
count = 0
for char in input_str:
    if char.isupper():
      count = count+1
      print(count)