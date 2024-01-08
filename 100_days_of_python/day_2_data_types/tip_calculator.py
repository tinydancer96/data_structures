print("Welcome to the tip calculator")

while True:
    try:
        bill = float(input("What was the total bill? "))
        tip = int(input("What percentage tip would you like to give? 10, 12, or 15 "))
        if tip not in {10, 12, 15}:
            raise ValueError("Invalid tip percentage")
        number_of_people = int(input("How many people are splitting the bill? "))
    except ValueError as e:
        print(f"Error: {e}. Please enter valid input.")
    else:
        individual_bill = (bill + (bill * (tip/100))) / number_of_people
        print(f"Each person owes £{individual_bill:.2f}")
        break
