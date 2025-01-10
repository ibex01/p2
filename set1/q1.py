# (a) Accept string input and remove unwanted characters
def process_input(user_input):
    filtered_string = ''.join([char for char in user_input if char.isalpha()])
    return filtered_string

# (b) Define the Caesar cipher function
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result

# (c) Encrypt and decrypt the text
def encrypt_decrypt():
    user_input = input("Enter a string (may include special characters, spaces, and numbers): ")
    filtered_string = process_input(user_input)
    print("Filtered String:", filtered_string)

    shift = 3
    encrypted_text = caesar_cipher(filtered_string, shift)
    print("Encrypted Text:", encrypted_text)

    decrypted_text = caesar_cipher(encrypted_text, -shift)
    print("Decrypted Text:", decrypted_text)

# Run Caesar cipher encryption and decryption
encrypt_decrypt()
