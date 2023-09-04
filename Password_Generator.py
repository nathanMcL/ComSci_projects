# This Password Generator:
# Uses random ascii, and numerical characters
# Chose length of password to generate.
# Can add more words to the list.
# Two words have a ~50 % chance to generate


import random
import string


# This function inserts a word into a password at a random location.
def insert_word(password, word):
    """
    Inserts a word into a password at a random location.

    Args:
        password (str): The password.
        word (str): The word to insert.

    Returns:
        str: The password with the word inserted.
    """
    index = random.randint(0, len(password))
    return password[:index] + word + password[index:]


# This function generates a password of a specified length.
def generate_password(length=15, add_words=["RaBBit", "crAp", "eGGs", "SaucEd"]):
    """
    Generates a password of a specified length.

    Args:
        length (int, optional): The length of the password. Defaults to 15.
        add_words (list, optional): A list of words to add to the password. Defaults to ["Rabbit", "crap"].

    Returns:
        str: The generated password.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))

    # Add words to the password at random locations.
    for word in add_words:
        if random.choice([True, False]):
            password = insert_word(password, word)

    return password


# This is the main function.
if __name__ == "__main__":
    # Generate a new password.
    new_password = generate_password()

    # Print the new password.
    print(f"Your new password is: {new_password}")