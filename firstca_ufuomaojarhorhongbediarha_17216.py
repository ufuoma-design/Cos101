number = int(input("ENTER A WHOLE NUMBER: "))

print()
print(f"MULTIPLICATION TABLE FOR {number}")
print("==================================")

 ,for multiplier in range(1, 13):
    result = number * multiplier
    print(f"{number} x {multiplier} = {result}")

print()
while True:
    close = input("PRESS 'e' TO END PROGRAM \n")
    if close == 'e':
        print("PROGRAM ENDED SUCCESFULLY")
        exit()
    else:
        print(close)
