from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, vehicle_id, name, price_per_day):
        self.vehicle_id = vehicle_id
        self.name = name
        self.price_per_day = price_per_day

    def get_rental_price(self):
            return self.price_per_day
    
    @abstractmethod
    def calculate_rent(self,days):
        pass
    
    
    def display_details(self):
        print("Vehicle NO:",self.vehicle_id)
        print("name:",self.name)
        print("Rental Price Per Day:",self.get_rental_price())