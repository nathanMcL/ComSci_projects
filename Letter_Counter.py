# The purpose of this program:
# Count the letters used,
# Count the total letters used

def count_letters(name):
    """
  This function counts the number of letters used in a string.

  Args:
    name: The string to count the letters in.

  Returns:
    A tuple of two dictionaries. The first dictionary contains the number of times each letter appears in the string. The second dictionary contains the total number of letters in the string.
  """

    # Create a dictionary to store the letter counts.
    letter_count = {}

    # Create a variable to store the total number of letters.
    total_count = 0

    # Iterate over each letter in the name.
    for letter in name:
        # Check if the letter is an alphabetic character.
        if letter.isalpha():
            # Convert the letter to lowercase.
            letter = letter.lower()

            # Increment the count of the letter in the dictionary.
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1

            # Increment the total count of letters.
            total_count += 1

    # Separate the vowels and consonants.
    vowels = []
    consonants = []
    for letter in name:
        if letter in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            vowels.append(letter)
        else:
            consonants.append(letter)

    # Return a tuple of the three values.
    return letter_count, total_count, vowels, consonants


# Get the name to be analyzed.
name = "Sparkling blue diamond"

# Count the letters in the name.
result, total_count, vowels, consonants = count_letters(name)

# Print the letter counts.
print(f"Letter counts in the name '{name}':")
for letter, count in sorted(result.items()):
    print(f"{letter}: {count}")

# Print the total number of letters.
print(f"Total count of letters: {total_count}")

# Print the vowels.
print("Vowels:", vowels)

# Print the consonants.
print("Consonants:", consonants)
