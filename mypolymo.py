class Vihicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        return "The engine is starting."
    def stop_engine(self):
        return "The engine stopped."
    def display_info(self):
        return f"Vehicle Info: {self.year} {self.make} {self.model}"
class Car(Vihicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Doors: {self.num_doors}"

class Motorcycle(Vihicle):
    def __init__(self, make, model, year, has_sidecar):
        super().__init__(make, model, year)
        self.has_sidecar = has_sidecar

    def display_info(self):
        base_info = super().display_info()
        sidecar_info = "with Sidecar" if self.has_sidecar else "without Sidecar"
        return f"{base_info}, {sidecar_info}"
car = Car("Toyota", "Camry", 2020, 4)
motorcycle = Motorcycle("Harley-Davidson", "Street 750", 2019, False)
print(car.display_info())
print(car.start_engine())
print(car.stop_engine())
print(motorcycle.display_info())
print(motorcycle.start_engine())
print(motorcycle.stop_engine())