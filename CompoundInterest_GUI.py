# Compound Interest GUI Calculator:
# Enter Principal amount.
# Enter interest rate.
# Enter time in years.
# Calculate option.

import tkinter as tk
from tkinter import ttk


def calculate():
    global result_label
    try:
        principle = float(principle_entry.get())
        rate = float(rate_entry.get())
        time = int(time_entry.get())
        if principle > 0 and rate > 0 and time > 0:
            total = principle * pow((1 + rate / 100), time)
            result_label.config(text=f"Balance after {time} years/s: ${total:.2f}")
        else:
            results_label.config(text="Inputs must be greater than zero")
    except ValueError:
        results_label.config(text="Invalid input, enter numerical values")
# 9/3/23 unsure how to resolve red squiggles.program runs.

# Initialize the Tkinter window
root = tk.Tk()
root.title("Compound Interest Calculator")

# Create Labels
ttk.Label(root, text="Principle amount:").grid(column=0, row=0)
ttk.Label(root, text="Interest rate:").grid(column=0, row=1)
ttk.Label(root, text="Time (years):").grid(column=0, row=2)

# Create entry widgets to accept input
principle_entry = ttk.Entry(root)
rate_entry = ttk.Entry(root)
time_entry = ttk.Entry(root)

# Place entry widgets
principle_entry.grid(column=1, row=0)
rate_entry.grid(column=1, row=1)
time_entry.grid(column=1, row=2)

# create button to calculate compound interest
calculate_button = ttk.Button(root, text="calculate", command=calculate)
calculate_button.grid(column=0, row=3, columnspan=2)

# Create label to display result
result_label = ttk.Label(root, text="")
result_label.grid(column=0, row=4, columnspan=2)

# Start event loop
root.mainloop()
