import random

while True:
    choice=int(input("What is the number that I am thinking right now? "))
    result = random.randint(1, 2)
    if choice == result:
        print("correct!")
        print(result)

    else:
        print("Wrong guess!")
        print(result)
        opt=input("Do you want to guess again? Y/N")
        if opt == 'Y':
            continue
        elif opt == 'N':
            break
        else:
            print("Wrong Choice!")
            continue