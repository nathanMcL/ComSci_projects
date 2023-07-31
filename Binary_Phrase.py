# This program translates a binary string to the correct phrase.

def binary_to_ascii(binary_string):
    """Translates a binary string into ASCII characters.

  Args:
    binary_string: A string of binary digits.

  Returns:
    A string of ASCII characters.
  """

    # This line creates an empty list to store the ASCII characters.
    ascii_characters = []

    # This loop iterates through the binary string, in groups of 8 bits.
    for i in range(0, len(binary_string), 8):
        # This line extracts a byte from the binary string.
        byte = binary_string[i:i + 8]

        # This line converts the byte to an ASCII character.
        ascii_character = chr(int(byte, 2))

        # This line appends the ASCII character to the list of ASCII characters.
        ascii_characters.append(ascii_character)

    # This line returns the string of ASCII characters.
    return ''.join(ascii_characters)


def main():
    # This line defines the binary string to be translated.
    binary_string = "010000010110110001101100001000000110010001100001011110010010000001100001011000110111010001101001011011110110111000111111"

    # This line calls the `binary_to_ascii()` function to convert the binary string to ASCII characters.
    ascii_characters = binary_to_ascii(binary_string)

    # This line prints the ASCII characters.
    print(ascii_characters)


if __name__ == "__main__":
    # This line calls the `main()` function.
    main()
