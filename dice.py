import random

"""This is the fucntion to generate random numbers"""

while True:
    choice=input("Do you want to roll dice? ")
    if choice == 'yes':
        result = random.randint(1,6)
        print("Here is the result: ", result)
    elif choice == 'no':
        print("Bye!!")
        break
    else:
        print("Wrong choice!")
        continue