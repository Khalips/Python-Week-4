# Error Handling Lab 🧪

# Ask the user for a filename
filename = input("Enter the filename to read: ")

try:
    # Try to open and read the file
    with open(filename, 'r') as f1:
        content = f1.read()
    
    print("File read successfully!")
    print("\nFile Content is in the new file\n")
    
    with open('output.txt', 'w') as f2:
        f2.write(content)

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except IOError:
    print(f"Error: The file '{filename}' could not be read.")
