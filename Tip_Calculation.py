# The Purpose of this program:
# prompt to enter an amount
# prompt to enter percentage
# prompt to split the bill

def tip_calculator(bill_amount, tip_percentage, number_of_people):
    """Calculates the tip amount, total bill amount, and per person amount.

  Args:
    bill_amount: The amount of the bill.
    tip_percentage: The tip percentage as a decimal.
    number_of_people: The number of people splitting the bill.

  Returns:
    A tuple of the tip amount, total bill amount, and per person amount.
  """

    tip = bill_amount * tip_percentage
    total = bill_amount + tip
    per_person_amount = total / number_of_people
    return tip, total, per_person_amount


def main():
    """Prompts the user for the bill amount, tip percentage, and number of people, then prints the tip, total amount,
    and per person amount."""

    bill_amount = float(input("Enter the bill amount: "))
    tip_percentage = float(input("Enter the tip percentage (e.g. .15, .18, .20): "))
    number_of_people = int(input("How many people are splitting the bill?: "))

    tip, total, per_person_amount = tip_calculator(bill_amount, tip_percentage, number_of_people)

    print("The tip is ${}, the total is ${}, and each person owes ${}".format(tip, total, per_person_amount))


if __name__ == "__main__":
    main()
