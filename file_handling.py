import csv

#file_location = input("Please enter the location of the csv file: ")

#f = path

def search_employee():
    f = "C:\\Users\\Amit.Banik\\Desktop\\test.csv"
    name = input("Enter employee name to be searched: ")
    print(type(name))
    try:
        with open(f) as f:
            reader=csv.reader(f)
            header = next(reader)
            data = [row for row in reader]
        #print("=============================")
        #print(header)
        #print("=============================")
        #print(type(data[0]))
            print(data[0])
        #print()
       #print()
        #b=data[0]
        #print(data[0][0])
        #print("We shall search for ",name)
            if name in data[0]:
            #print(name, "found!!")
                print("Employee ID is: ",(data[0][0]))
                print("Name of the Employee is: ", (data[0][1]))
                print("Gender of the Employee is: ", (data[0][2]))
                print("Pickup location of the Employee is: ", (data[0][3]))
                print("Shift start time of the Employee is: ", (data[0][4]))
                print("Shift end time of the Employee is: ", (data[0][7]))
            else:
                print(name, "not found!!")
    #print(type(file_location))

    except Exception as e:
        print(e)
        print("Please provide a proper file path")


search_employee()




while True:
    choice = input("Do you want to search another employee?: ")
    if choice == 'no':
        break
    elif choice == 'yes':
        print("To exit you have to enter 'no'")
        search_employee()
    else:
        print("Invalid option!!")
        continue