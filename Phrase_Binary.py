# The purpose of this program is to convert a phrase into a binary string.

def cpb(phrase):
    """Converts a short phrase to binary.

  Args:
    phrase: A string containing the phrase to be converted.

  Returns:
    A string containing the binary representation of the phrase.
  """

    # This line creates an empty string to store the binary representation of the phrase.
    binary_phrase = ""

    # This loop iterates through the phrase, one character at a time.
    for character in phrase:
        # This line gets the ASCII code of the character.
        ascii_code = ord(character)

        # This line converts the ASCII code to a binary string.
        binary_code = bin(ascii_code)[2:]

        # This line pads the binary string with zeros to make it 8 characters long.
        binary_code = "0" * (8 - len(binary_code)) + binary_code

        # This line appends the binary string to the binary representation of the phrase.
        binary_phrase += binary_code

    # This line returns the binary representation of the phrase.
    return binary_phrase


# This line defines the phrase to be converted.
phrase = "All day action?"

# This line calls the `cpb()` function to convert the phrase to a binary string.
binary_phrase = cpb(phrase)

# This line prints the binary representation of the phrase.
print(binary_phrase)
