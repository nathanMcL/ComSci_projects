# GUI tip calculator
# The purpose of this program:
# Enter the bill amount,
# set the tip amount (default is 15%)
# returns suggested tip amount

import tkinter as tk
from tkinter import ttk


# Function to calculate the tip and total the amount
def calculate(*args):
    try:
        bill_amount = float(bill_entry.get())
        tip_percentage = float(tip_var.get())
    except ValueError:
        results_label.config(text="Invalid Input")
        return

    tip_amount = bill_amount * (tip_percentage / 100)
    total_amount = bill_amount + tip_amount

    results_label.config(text=f"Tip amount: ${tip_amount:.2f}\nTotal Amount: ${total_amount:.2f}")
    #results_label.config(text="")


# Create the main window
window = tk.Tk()
window.title("Tip Calculator")

# Create and place widgets
bill_label = ttk.Label(window, text="Bill Amount:")
bill_label.grid(column=0, row=0)

bill_entry = ttk.Entry(window)
bill_entry.grid(column=1, row=0)

tip_label = ttk.Label(window, text="Tip Percentage:")
tip_label.grid(column=0, row=1)

tip_var = tk.DoubleVar()
tip_var.set(15)  # Default tip percentage is set to 15%
tip_slider = ttk.Scale(window, from_=0, to=100, variable=tip_var, orient="horizontal")
tip_slider.grid(column=1, row=1)

calculate_button = ttk.Button(window, text="Calculate", command=calculate)
calculate_button.config(command=calculate)
calculate_button.grid(column=0, row=2, columnspan=2)

results_label = ttk.Label(window, text="")
results_label.grid(column=0, row=3, columnspan=2)

# Bind the value_changed event of the tip_var variable to the calculate function
tip_var.trace("w", calculate)

# Starts the main loop
window.mainloop()
