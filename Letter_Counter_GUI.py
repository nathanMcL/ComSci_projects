# The purpose of this GUI program:
# Count the number of letters, vowels, and consonants in a phrase.

import tkinter as tk
from tkinter import ttk


# This function processes the user input and updates the labels with the results.
def process_input():
    phrase = user_input.get()

    # Count all the letters in the phrase.
    all_letters = [char for char in phrase if char.isalpha()]
    total_letters.set(f"Total letters: {len(all_letters)}")

    # Separate the vowels and consonants.
    vowels = "a, e, i, o, u, A, E, I, O, U"
    vowel_count = 0
    consonant_count = 0
    vowel_str = ''
    consonant_str = ''

    for letter in all_letters:
        if letter in vowels:
            vowel_count += 1
            vowel_str += letter
        else:
            consonant_count += 1
            consonant_str += letter

    # Update the labels with the results.
    vowels_label.config(text=f"Vowels ({vowel_count}): {vowel_str}")
    consonants_label.config(text=f"Consonants ({consonant_count}): {consonant_str}")


# Create the main window.
root = tk.Tk()
root.title('Count Letters, Vowels, and Consonants')

# Create the widgets.
user_input = tk.StringVar()
total_letters = tk.StringVar()
total_letters.set("Total letters: 0")

input_entry = ttk.Entry(root, textvariable=user_input, width=50)
input_button = ttk.Button(root, text='Process', command=process_input)
total_letters_label = ttk.Label(root, textvariable=total_letters)
vowels_label = ttk.Label(root, text='Vowels: ')
consonants_label = ttk.Label(root, text='Consonants: ')

# Place the widgets.
input_entry.grid(row=0, column=0, padx=10, pady=10)
input_button.grid(row=0, column=1, padx=10, pady=10)
total_letters_label.grid(row=1, columnspan=2, padx=10, pady=10)
vowels_label.grid(row=3, columnspan=2, padx=10, pady=10)

# Start the GUI event loop.
root.mainloop()
