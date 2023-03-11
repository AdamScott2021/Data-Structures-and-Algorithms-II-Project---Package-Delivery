# This is the packages class, it is responsible for keeping track of all information about packages
# Time Complexity: O(1)
class Packages:
    def __init__(self, id_Num, address, city, state, zip_Code, delivery_Deadline, weight, status):
        self.id_Num = id_Num
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip_Code
        self.delivery_Deadline = delivery_Deadline
        self.package_Weight = weight
        self.package_Status = status
        self.Departure_Time = None
        self.Delivery_Time = None

    # Time Complexity: O(1)
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, Truck %s" % (self.id_Num, self.address, self.city, self.state,
                                                             self.zip, self.delivery_Deadline, self.package_Weight,
                                                             self.package_Status, self.truck_Num)

    # This is a function that updates the packages status throughout the program
    # Time Complexity: O(1)
    def update_Package_Status(self, change_Status):

        if change_Status < self.Departure_Time:
            self.package_Status = "At The Hub"
        elif change_Status < self.Delivery_Time:
            self.package_Status = "En Route"
        else:
            self.package_Status = "Delivered at %s" % self.Delivery_Time
