from Vehicle import Vehicle

class Bike(Vehicle):
    def calculate_rent(self, days):
        return  (self.get_rental_price() * days + 100)