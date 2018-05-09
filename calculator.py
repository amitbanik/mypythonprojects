from addition import add
from substract import subs
from multi import mul
from division import div

def calc():

#choice=int(input("Press \n1. ADD \n2. DEDUCT \n3. MULTIPLY \n4. DIVISION\n"))

#print(type(choice))


#def option():
    while True:
        print("Welcome to the calculator")
        choice = input("Press \n1. ADD \n2. DEDUCT \n3. MULTIPLY \n4. DIVISION\nq. QUIT\n")
        a = int(input("Enter 1st number: "))
        b = int(input("Enter 2nd number: "))

        print("You have entered ", a, "and", b)
        #print("What do you want to do?")

        if choice == '1':
            print("You have entered ", choice)
            print("The sum of ", a, "and ", b, "is: ", add(a,b))
        #option()
        elif choice == '2':
            print("You have entered ", choice)
            print("The difference of ", a, "and ", b, "is: ", subs(a, b))
        #option()
        elif choice == '3':
            print("You have entered ", choice)
            print("The multiplication of ", a, "and ", b, "is: ", mul(a, b))
        #option()
        elif choice == '4':
            print("You have entered ", choice)
            print("The division of ", a, "and ", b, "is: ", div(a, b))
        #option()
        elif choice == 'q':
            print("You have entered ", choice)
            print("exiting!")
            break
        else:
            print("WRONG CHOICE!!!")
            continue


calc()




#while True:
 #       opt = input("Do you want to repeat?: Y/N\n")
  #      if opt == 'Y':
   #         calc()
    #    elif opt == 'N':
     #       print("Bye!!")
      #      break
       # else:
        #    print("invalid option!")
         #   continue








