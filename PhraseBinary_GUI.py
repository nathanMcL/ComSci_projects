# This program converts a phrase to binary.

import tkinter as tk
from tkinter import ttk


# This function converts a phrase to binary.
def cpb(phrase):
    """
    Convert a phrase to binary.

    Args:
        phrase (str): The phrase to convert.

    Returns:
        str: The binary string.
    """
    binary_phrase = ""
    for character in phrase:
        ascii_code = ord(character)
        binary_code = bin(ascii_code)[2:]
        # Pad the binary code with zeros to make it 8 characters long.
        binary_code = "0" * (8 - len(binary_code)) + binary_code
        binary_phrase += binary_code
    return binary_phrase


# This function is called when the user clicks the "Convert" button.
def convert_to_binary():
    """
    Convert the phrase in the entry box to binary.
    """
    phrase = phrase_entry.get()
    binary_result = cpb(phrase)
    binary_label.config(text=f"Binary Result: {binary_result}")

    # Print the binary result to the console
    print(f"Binary Result: {binary_result}")


# Create the main window.
root = tk.Tk()
root.title("Phrase to Binary Converter")

# Create a label to instruct the user.
instruction_label = ttk.Label(root, text="Enter a phrase:")
instruction_label.pack(padx=10, pady=5)

# Create an entry box for the user to enter a phrase.
phrase_entry = ttk.Entry(root, width=50)
phrase_entry.pack(padx=10, pady=5)

# Create a button to perform the conversion.
convert_button = ttk.Button(root, text="Convert", command=convert_to_binary)
convert_button.pack(padx=10, pady=10)

# Create a label to display the result.
binary_label = ttk.Label(root, text="Binary Result:")
binary_label.pack(padx=10, pady=10)

# Start the Tkinter event loop.
root.mainloop()