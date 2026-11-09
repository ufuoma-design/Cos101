# This program calculates total weekly expenses for a student on campus based on the information provided

#input
name = input("Enter the student name: ")
daily_transport = float(input("Enter amout spent on transport daily: "))
daily_feeding = float(input("Enter amount spent on feeding daily: "))
days_on_campus = int(input("Enter number of days on campus: "))
other_expenses = float(input("Enter any other miscellaneous expenses for the week: "))

#process
transport_total = daily_transport * days_on_campus
feeding_total = daily_feeding * days_on_campus
weekly_total = transport_total + feeding_total + other_expenses

#output
print("\n--- WEEKLY EXPENSES SUMMARY ---")
print("Student Name: ", name)
print("Transport Total: NGN", transport_total)
print("Feeding Total: NGN", feeding_total)
print("Other expenses: NGN", other_expenses)
print("Weekly Total: NGN", weekly_total)

#When you use the int() it only allows the input to be integers
#string() allows the input to be only letters
#The float() function in Python converts a number or a string containing a number into a floating-point number (a number with a decimal point)


#SIMON, Emmanuel Kwayil
#VUG/SEN/26/15906
