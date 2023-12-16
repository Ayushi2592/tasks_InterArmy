import random
import string

def generate_key():
    characters = string.ascii_letters + string.digits + string.punctuation + string.whitespace
    shuffled_characters = random.sample(characters, len(characters))
    return dict(zip(characters, shuffled_characters))

def encrypt(message, key):
    # Use the key to substitute each character in the message
    encrypted_message = ''.join(key.get(char, char) for char in message)
    return encrypted_message

def decrypt(encrypted_message, key):
    # Reverse the key to decrypt the message
    reverse_key = {v: k for k, v in key.items()}
    decrypted_message = ''.join(reverse_key.get(char, char) for char in encrypted_message)
    return decrypted_message

def main():
    print("=== Encryption and Decryption ===")

    # Generate a random key
    key = generate_key()

    # Get user input
    message = input("Enter a message: ")

    # Encrypt the message
    encrypted_message = encrypt(message, key)

    print("\nEncryption Result:")
    print(f"Original message: {message}")
    print(f"Encrypted message: {encrypted_message}")

    # Decrypt the message
    decrypted_message = decrypt(encrypted_message, key)

    print("\nDecryption Result:")
    print(f"Encrypted message: {encrypted_message}")
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
