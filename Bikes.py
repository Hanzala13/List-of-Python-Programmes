# Base class
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

# Derived class: Car
class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors

    def display_info(self):
        super().display_info()
        print(f"Type: Car | Doors: {self.doors}")

# Derived class: Truck
class Truck(Vehicle):
    def __init__(self, brand, model, year, payload_capacity):
        super().__init__(brand, model, year)
        self.payload_capacity = payload_capacity

    def display_info(self):
        super().display_info()
        print(f"Type: Truck | Payload Capacity: {self.payload_capacity} kg")

# Derived class: Bike
class Bike(Vehicle):
    def __init__(self, brand, model, year, bike_type):
        super().__init__(brand, model, year)
        self.bike_type = bike_type  # e.g., 'Mountain', 'Sport', 'Cruiser'

    def display_info(self):
        super().display_info()
        print(f"Type: Bike | Bike Type: {self.bike_type}")

# Example usage
if __name__ == "__main__":
    car = Car("Toyota", "Corolla", 2022, 4)
    truck = Truck("Ford", "F-150", 2021, 1300)
    bike = Bike("Yamaha", "MT-15", 2023, "Sport")

    print("--- Car Info ---")
    car.display_info()

    print("\n--- Truck Info ---")
    truck.display_info()

    print("\n--- Bike Info ---")
    bike.display_info()
