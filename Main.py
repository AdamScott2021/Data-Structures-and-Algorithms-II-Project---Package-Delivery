# Adam Scott - ID Number: 001423886

import csv
import datetime
import Trucks
import HashMap
import Packages
from builtins import ValueError

# These are the truck objects
# Time Complexity: O(1)
first_Truck = Trucks.Trucks(1, [15, 37, 33, 1, 14, 16, 20, 29, 30, 34, 13, 19], 4,
                            "4001 South 700 East 84107", datetime.timedelta(hours=8, minutes=0), 16, 18)
second_Truck = Trucks.Trucks(2, [3, 18, 36, 38, 35, 39, 2, 4, 5, 7, 8, 24], 6,
                             "4001 South 700 East 84107", datetime.timedelta(hours=8, minutes=0), 16, 18)
third_Truck = Trucks.Trucks(3, [31, 40, 10, 11, 12, 17, 21, 22, 23, 26, 27, 32, 25, 28, 6, 9], 4,
                            "4001 South 700 East 84107", datetime.timedelta(hours=9, minutes=5), 16, 18)


# This function reads the package data csv file and creates package objects containing the information for each package
# Time Complexity: O(N)
def load_Package_Info(package_Data):
    with open(package_Data) as package_Data:
        packageData = csv.reader(package_Data, delimiter=',')

        for package in packageData:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZip = package[4]
            pDeadline = package[5]
            pWeight = package[6]
            pStatus = "At Hub"

            package = Packages.Packages(pID, pAddress, pCity, pState, pZip, pDeadline, pWeight, pStatus)
            HashMap.my_Hash.insert(pID, package)


load_Package_Info("Package_Data.csv")


# This function references the address data csv file and determines the delivery address for each package
# Time Complexity: O(N)
def address_Lookup(address):
    with open("Address_Data.csv") as Address_File:
        Address_Data_CSV = csv.reader(Address_File)
        Address_Data_CSV = list(Address_Data_CSV)
        for i, row in enumerate(Address_Data_CSV):
            if address in row[1]:
                return i


# This function looks at the distance data csv file and determines the distance between addresses
# Time Complexity: O(1)
def Distance(address_X, address_Y):
    with open("Distance_Data.csv") as Distance_File:
        distances = csv.reader(Distance_File)
        distances = list(distances)
    distance_Between = distances[address_X][address_Y]
    if distance_Between == '':
        distance_Between = distances[address_Y][address_X]
    return float(distance_Between)


# This is the greedy_Algorithm. it sorts packages by comparing the current address to the next address and
# determining the distance then it orders packages by finding the closest one to the current package
# Time Complexity: O(N^2)
def greedy_algorithm(start_address, start_Packages):
    current_address = start_address
    current_Packages = start_Packages
    visited_Packages = []
    total_Distance = 0.0
    while len(current_Packages) > 0:
        next_Package = HashMap.my_Hash.search(current_Packages[0])
        next_distance = Distance(address_Lookup(current_address), address_Lookup(next_Package.address))
        for package_ID in current_Packages[1:]:
            current_Package = HashMap.my_Hash.search(package_ID)
            current_distance = Distance(address_Lookup(current_address), address_Lookup(current_Package.address))
            if current_distance < next_distance:
                next_Package = current_Package
                next_distance = current_distance
            if package_ID == 25:
                next_Package = current_Package
                next_distance = current_distance
                break
        current_address = next_Package.address
        visited_Packages.append(next_Package.id_Num)
        current_Packages.remove(next_Package.id_Num)
        total_Distance += next_distance
    return visited_Packages, total_Distance


A = greedy_algorithm(first_Truck.delivery_Address, first_Truck.packages_In_Truck)
first_Truck.total_Mileage = A[1]
first_Truck.packages_In_Truck = A[0]
B = greedy_algorithm(second_Truck.delivery_Address, second_Truck.packages_In_Truck)
second_Truck.total_Mileage = B[1]
second_Truck.packages_In_Truck = B[0]
C = greedy_algorithm(third_Truck.delivery_Address, third_Truck.packages_In_Truck)
third_Truck.total_Mileage = C[1]
third_Truck.packages_In_Truck = C[0]


# This update_Time function updates all packages by referencing their ID numbers and updates the time to display the
# time they were delivered
# Time Complexity: O(N)
def update_Time(truck):
    for package_ID in truck.packages_In_Truck:
        departure_Package = HashMap.my_Hash.search(package_ID)
        departure_Package.Departure_Time = truck.departure_Time
        departure_Package.truck_Num = truck.truck_Num
    delivery_Time = truck.departure_Time
    for package in truck.packages_In_Truck:
        current_package = HashMap.my_Hash.search(package)
        distance = Distance(address_Lookup(truck.delivery_Address), address_Lookup(current_package.address))
        delivery_Time += datetime.timedelta(hours=distance / truck.max_Speed)
        current_package.Delivery_Time = delivery_Time
        truck.delivery_Address = current_package.address


update_Time(first_Truck)
update_Time(second_Truck)
update_Time(third_Truck)


# This function calculates the distance each truck has travelled and adds them together in order to calculate total
# mileage
# Time Complexity: O(1)
def Mileage():
    print("The Current Mileage is: ", first_Truck.total_Mileage + second_Truck.total_Mileage +
          third_Truck.total_Mileage)
    text = input("If you would like to exit, type 'Exit'. To view the status of packages, type 'Status': ")
    if text == "Status":
        Status()
    else:
        print("Goodbye")
        exit()


# This is part of the user interface. it is specifically used for displaying the status of packages and prompting
# the user
# Time Complexity: O(N)
def Status():
    text = input("Would you like to view a specific package or all packages? (Type 'One' or 'All'): ")
    if text == "One":
        try:
            package_Num = input("Please enter the ID number of the package you want to view: ")
            selected_Package = HashMap.my_Hash.search(int(package_Num))
            time = input("Please Enter A Time In The format 'HH:MM': ")
            (h, m) = time.split(":")
            convert_Time = datetime.timedelta(hours=int(h), minutes=int(m))
            package = HashMap.my_Hash.search(int(package_Num))
            package.update_Package_Status(convert_Time)
            print(str(selected_Package))
            text = input("If you would like to view the status of another package type 'Yes' or 'No': ")
            if text == "Yes":
                Status()
            else:
                print("Goodbye")
                exit()
        except ValueError:
            print("Invalid Entry, please try again")
            Status()
    if text == "All":
        time = input("Please Enter A Time In The format 'HH:MM': ")
        (h, m) = time.split(":")
        convert_Time = datetime.timedelta(hours=int(h), minutes=int(m))
        for i in range(1, 41):
            package = HashMap.my_Hash.search(int(i))
            package.update_Package_Status(convert_Time)
            print("Package: {}".format(HashMap.my_Hash.search(i)))
        text = input("If you would like to view the status of another package type 'Yes' or 'No': ")
        if text == "Yes":
            Status()
        elif text == "No":
            print("Goodbye")
            exit()
        else:
            print("Invalid entry, please try again")
            Status()


# This is another part of the user interface used to choose between miles or package status
# Time Complexity: O(1)
def Main():
    print("To view the current total mileage type 'Mileage'")
    print("To view package status type 'Status'")
    text = input("Which would you like to view?: ")
    if text == "Mileage":
        Mileage()
    elif text == "Status":
        Status()
    else:
        print("Invalid entry, please try again")
        Main()


# This is the main class. I separated it like this in order to handle exceptions better
# Time Complexity: O(1)
class main_Class:
    print("Welcome to the WGU Mail Carrier Service")
    Main()
