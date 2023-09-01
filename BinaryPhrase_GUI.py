# This program converts a binary string to ASCII.

import tkinter as tk
from tkinter import ttk


# This function converts a binary string to ASCII.
def binary_to_ascii(binary_string):
    """
    Convert a binary string to ASCII.

    Args:
        binary_string (str): The binary string to convert.

    Returns:
        str: The ASCII string.
    """
    ascii_characters = []
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i + 8]
        ascii_character = chr(int(byte, 2))
        ascii_characters.append(ascii_character)
    return ''.join(ascii_characters)


# This function is called when the user clicks the "Convert" button.
def convert_binary():
    """
    Convert the binary string in the entry box to ASCII.
    """
    binary_string = binary_entry.get()
    ascii_result = binary_to_ascii(binary_string)
    ascii_label.config(text=f"ASCII Result: {ascii_result}")


# Create the main window.
root = tk.Tk()
root.title("Binary to ASCII Converter")

# Create a label to instruct the user.
instruction_label = ttk.Label(root, text="Enter a binary string:")
instruction_label.pack(padx=10, pady=5)

# Create an entry box for the user to enter a binary string.
binary_entry = ttk.Entry(root, width=80)
binary_entry.pack(padx=10, pady=5)

# Create a button to perform the conversion.
convert_button = ttk.Button(root, text="Convert", command=convert_binary)
convert_button.pack(padx=10, pady=10)

# Create a label to display the result.
ascii_label = ttk.Label(root, text="ASCII Result:")
ascii_label.pack(padx=10, pady=10)

# Start the Tkinter event loop.
root.mainloop()