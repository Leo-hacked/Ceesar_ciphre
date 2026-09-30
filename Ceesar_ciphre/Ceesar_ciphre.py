#Leo Esparza
#Dr.Giles Cit-104
#Progressive offset Caesar cipher program
# Open and read the quote file
f = open("quote.txt", "r")
plaintext = f.read()
f.close()

# Display the original quote
print("Original quote:")
print(plaintext)

# Get a valid offset from the user
distance = int(input("Enter an integer between 1 and 20: "))

# Validate the offset
while distance < 1 or distance > 20:
    print("Please enter a number between 1 and 20.")
    distance = int(input("Enter an integer between 1 and 20: "))

# Encrypt the quote
code = ""

for index, ch in enumerate(plaintext):
    current_distance = distance + (index % 3)

    if 'a' <= ch <= 'z':
        ordvalue = ord(ch)
        ciphervalue = ordvalue + current_distance

        if ciphervalue > ord('z'):
            ciphervalue = ord('a') + (ciphervalue - ord('z') - 1)

        code += chr(ciphervalue)
    else:
        code += ch

# Display the encrypted quote
print("\nEncrypted quote:")
print(code)

# Save the encrypted quote
output_file = open("encrypted_quote.txt", "w")
output_file.write(code)
output_file.close()

print("The encrypted quote has been saved to 'encrypted_quote.txt'.")
