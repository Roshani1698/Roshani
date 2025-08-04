# 1. Car Mileage Tracker

class car:
    def __init__(self, brand, model, mileage):
        self.brand=brand
        self.model=model
        self.mileage=mileage

    def drive(self,km):
        self.mileage += km

    def service(self):
        self.mileage = 0

    def display(self):
        print(f"brand: {self.brand}, model:{self.model}, mileage:{self.mileage} km")


car1 = car("Toyoto", "Inova", 12000)
car2 = car("Honda", "City", 8000)

car1.drive(1000)
car2.drive(500)

car1.service()

car1.display()
car2.display()