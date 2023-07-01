# This program generates a range of random binary numbers with the decimal equivalent
# Prompts user to enter a binary number
# If inputted binary number is equal to one of the random binary decimal equivalents, a message is printed



import random


# Generate random binary row
def GRBR():
    row = []
    for i in range(20):
        row.append(random.randint(0, 1))
    return row


# Random Row And Column
def RRAC():
    row = GRBR()
    print("Row:", row)
    print("Column:", *row)
    print("Decimal: ", sum(row))
    print()


# Set Binary Range
for i in range(20):
    RRAC()


# User Binary Input
def UBI():
    binary_number = input("Enter a binary number: ")
    binary_list = list(binary_number)
    decimal_number = 0
    for i in range(len(binary_list)):
        if binary_list[i] != '':
            decimal_number += int(binary_list[i]) * 2 ** (len(binary_list) - i - 1)
    if decimal_number == decimal_number:
        print("Hello!", decimal_number)
    else:
        print("The decimal equivalent of the binary number is", decimal_number)


# Main
if __name__ == "__main__":
    UBI()
