'''
count = 20
for num in range(5):
    count = count + 1
    print(count)



#num = 0
#for num in range (2,20,2):
   # print(num)
# 1 is the strating piont
# 20 is the stoping point
# 2 is the stepping point
'''


number = int(input("Enter a number between 1-12: "))
print(f"This is the multiplication table for {number}")
print()
print()
print()
while number <= 1:
    print("Your number must be higher than 1 or press 5 to exit !")
    if number > 12:
        print("Your number should not be higher than 12")
    else:
        for num in range(1,13):
            answer = number * num
            print(f" {number} * {num} = {answer}")



























































































































