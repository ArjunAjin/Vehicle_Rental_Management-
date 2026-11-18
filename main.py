from Vehicle import Vehicle
from Car import Car
from Bike import Bike


print("____________CAR DETAILS______________")

car = Car("KL 34 361","BMW",896)
car.display_details()

car.calculate_rent(3)
print("Rent for three days:",car.calculate_rent(3))

print("___________BIKE DETAILS______________")

bike = Bike("KL 33 A 9651","Splendor",678)
bike.display_details()
bike.calculate_rent(3)
print("Bike Rent for 3 Days:",bike.calculate_rent(3))