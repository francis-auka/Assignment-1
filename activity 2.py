# Activity 2: Simple Vehicle Polymorphism

class Vehicle:
    def move(self):
        return "The vehicle is moving."

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚢"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

# Demo polymorphism
vehicles = [Car(), Boat(), Plane()]

for vehicle in vehicles:
    print(vehicle.move())