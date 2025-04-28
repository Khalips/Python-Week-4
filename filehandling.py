# File Read & Write Challenge 🖋️

# open the file and read the contents of input.txt file
with open('input.txt', 'r') as file:
    content = file.read()                #File contents stored in this variable

# Convert all text to uppercase (modifying the file)
uppercase_content = content.upper()

# open a file and write the uppercase content to the new file named output.txt
with open('output.txt', 'w') as file:
    file.write(uppercase_content)

# Print the success message
print("Success! 'output.txt' has been created with the modified content.")
