# Fibonacci sequence calculator GUI
# Enter a positive number
# Generate the Fibonacci sequence option


import tkinter as tk
from tkinter import ttk


# Your Fibonacci function
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Function to handle button click
def generate_fibonacci():
    try:
        n = int(n_entry.get())
        if n >= 0:
            fibonacci_sequence = []
            for i in range(n):
                fibonacci_sequence.append(fibonacci(i))
            result_label.config(text=f"The Fibonacci sequence is:\n {fibonacci_sequence}")
        else:
            result_label.config(text="Please enter a non-negative integer")
    except ValueError:
        result_label.config(text="Invalid input, enter a non-negative integer")


# Initialize the Tkinter window
root = tk.Tk()
root.title("Fibonacci Sequence Generator")

# Create label
ttk.Label(root, text="Enter a number:").grid(column=0, row=0)

# Create entry widget
n_entry = ttk.Entry(root)
n_entry.grid(column=1, row=0)

# Create button to generate Fibonacci sequence
generate_button = ttk.Button(root, text="Generate", command=generate_fibonacci)
generate_button.grid(column=0, row=1, columnspan=2)

# Create label to display result
result_label = ttk.Label(root, text="")
result_label.grid(column=0, row=2, columnspan=2)

# Start the Tkinter event loop
root.mainloop()
