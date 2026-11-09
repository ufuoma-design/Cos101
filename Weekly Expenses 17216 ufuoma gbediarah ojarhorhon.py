'''
            THIS CODE SHOWS AND INTERACTS WITH THE USER
                I USED 

'''

Question = input("Do you school in abuja    Yes/No:   ")
University = input("Name of your university: ")
Department = input("What is your department: ")
Name = input("What is your name: ")

print()
print()
                       

print()
tp = float(input("How much do you spend on transport: "))
print()
food = float(input("How much do you spend on feeding: "))

print()
clothing = float(input("How much do you spend on clothes: "))
print()
days = int(input("How many days have you spent in the university: "))
print()
other_exp = float(input("How much have you spent on other things: "))


trans_tot = days*tp
feeding_tot = days*food 
clothing_tot = days*clothing
other_exps = days*other_exp
print()
print()
Total=trans_tot + feeding_tot + clothing_tot

print(f"Your transport total is: {trans_tot}")
print(f"Your feeding total is: {feeding_tot}")
print(f"Your clothing total is: {clothing_tot}")

print(f"Your total expenses sums up to: {Total}  for the number of days you have spent")

(quit)




















































































