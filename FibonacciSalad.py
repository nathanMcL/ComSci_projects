from fibonacci import fibonacci


def encrypt(message):
    fibonacci_sequence = []
    for i, char in enumerate(message):
        fibonacci_sequence.append(fibonacci(i))

    ciphertext = ""
    for char in message:
        if char.isalpha():
            char_value = ord(char.lower()) - ord('a')
            ciphertext += str(fibonacci_sequence[char_value])
        else:
            ciphertext += char

    return ciphertext


def decrypt(ciphertext):
    fibonacci_sequence = []
    for i, char in enumerate(ciphertext):
        fibonacci_sequence.append(fibonacci(i))

    plaintext = ""
    for char in ciphertext:
        if char.isnumeric():
            char_value = int(char)
            plaintext += chr(fibonacci_sequence.index(char_value) + ord('a'))
        else:
            plaintext += char

    return plaintext


if __name__ == "__main__":
    message = input("Enter the message to encrypt: ")
    ciphertext = encrypt(message)
    print("The encrypted message is:", ciphertext)

    plaintext = decrypt(ciphertext)
    print("The decrypted message is:", plaintext)
