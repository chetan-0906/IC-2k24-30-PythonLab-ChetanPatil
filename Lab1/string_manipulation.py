# Take a full name as input and print it in uppercase, lowercase, reversed form and its length
name = input("Enter your full name: ")

print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Reversed:", name[::-1])
print("Length:", len(name))