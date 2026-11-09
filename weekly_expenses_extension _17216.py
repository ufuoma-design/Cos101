# This program calculates total weekly expenses for a student on campus
# and compares the total expenses with the student's weekly budget.

# INPUT
name = input("Enter the student name: ")

daily_transport = int(input("Enter amount spent on transport daily (NGN): "))
daily_feeding = int(input("Enter amount spent on feeding daily (NGN): "))
days_on_campus = int(input("Enter number of days on campus: "))
other_expenses = int(input("Enter other miscellaneous expenses for the week (NGN): "))

# INPUT VALIDATION
if daily_transport < 0:
    print("Invalid input! Transport expenses cannot be negative.")

elif daily_feeding < 0:
    print("Invalid input! Feeding expenses cannot be negative.")

elif days_on_campus < 0:
    print("Invalid input! Number of days cannot be negative.")

elif other_expenses < 0:
    print("Invalid input! Other expenses cannot be negative.")

else:

    # PROCESS
    transport_total = daily_transport * days_on_campus
    feeding_total = daily_feeding * days_on_campus
    weekly_total = transport_total + feeding_total + other_expenses

    # DISPLAY EXPENSE SUMMARY
    print("\n--- WEEKLY EXPENSES SUMMARY ---")
    print("Student Name:", name)
    print("Transport Total: NGN", transport_total)
    print("Feeding Total: NGN", feeding_total)
    print("Other Expenses: NGN", other_expenses)
    print("Weekly Total: NGN", weekly_total)

    # INPUT WEEKLY BUDGET
    weekly_budget = int(input("\nEnter your weekly budget (NGN): "))

    # BUDGET VALIDATION AND COMPARISON
    if weekly_budget < 0:
        print("Invalid input! Your budget cannot be negative.")

    elif weekly_total < weekly_budget:
        remaining = weekly_budget - weekly_total
        print("\nStatus: Within budget")
        print("Amount remaining: NGN", remaining)

    elif weekly_total == weekly_budget:
        print("\nStatus: Exactly on budget")
        print("Amount remaining: NGN 0")

    else:
        exceeded = weekly_total - weekly_budget
        print("\nStatus: Over budget")
        print("Amount exceeded: NGN", exceeded)




