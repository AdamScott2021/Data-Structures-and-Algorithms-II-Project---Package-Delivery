# This is the Trucks class, it is responsible for keeping track of all the trucks throughout the program
# Time Complexity: O(1)
class Trucks:
    def __init__(self, truck_Num, packages_In_Truck, total_Mileage, delivery_Address, departure_Time, max_Packages,
                 truck_Speed):
        self.packages_In_Truck = packages_In_Truck
        self.total_Mileage = total_Mileage
        self.delivery_Address = delivery_Address
        self.departure_Time = departure_Time
        self.delivery_Time = departure_Time
        self.truck_Capacity = max_Packages
        self.max_Speed = truck_Speed
        self.truck_Num = truck_Num

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.packages_In_Truck, self.total_Mileage, self.delivery_Address,
                                               self.departure_Time, self.truck_Capacity, self.max_Speed,
                                               self.delivery_Time)
