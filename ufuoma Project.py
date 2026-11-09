
print("                                          DAILY SALES SUMMARY    ")
print("                   ====================================================================")
print("")
print("")
print("")

days = int(input("Enter number days you have been selling: "))
while days <= 0:
    print("Invalid input. Input the proper amount of days")
    days = int(input("Enter the number of days"))

total_sales = 0
high_sales = 0
low_sales = 0

for day in range(1, days + 1):
    sales = float(input(f"Enter sales for day" + str(day) + ":"))

    while sales < 0:
        print("Sales cannot be negative.")
        sales = float(input("Enter sales again: "))

total_sales = total_sales + sales

if sales >= 10000:
    high_sales = high_sales + 1

elif sales < 10000:
    low_sales = low_sales + 1
print()
print()
average = total_sales / days
print("---------------SALES REPORT---------------")
print(f"Total sales:                                {total_sales}.2f")
print(f"Average daily sales:                        {average}.2f")
print(f"Days with sales of at least NGN10,000:      {high_sales}")
print(f"Days with below NGN10,000:                  {low_sales}")













































