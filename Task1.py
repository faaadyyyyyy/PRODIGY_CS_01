def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Non-alphabetical characters remain unchanged
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)


def caesar_cipher():
    while True:
        choice = input("Type 'e' to encrypt or 'd' to decrypt: ").strip().lower()
        if choice not in ['e', 'd']:
            print("Invalid choice. Please select 'encrypt' or 'decrypt'.")
            continue
        
        text = input("Enter your text: ")
        shift = int(input("Enter the shift value: "))

        if choice == 'e':
            result = encrypt(text, shift)
            print(f"Encrypted text: {result}")
        elif choice == 'd':
            result = decrypt(text, shift)
            print(f"Decrypted text: {result}")

        retry = input("Do you want to perform another operation? (yes/no): ").strip().lower()
        if retry != 'yes':
            print("ThankYou!")
            break
if __name__ == "__main__":
    caesar_cipher()
