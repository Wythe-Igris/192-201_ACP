"""Classes for the CampusWheels vehicle-rental demonstration."""


class Vehicle:
    def __init__(self, make, model, plate):
        self.make = make
        self.model = model
        self.plate = plate
        self.is_rented = False

    def rent(self):
        self.is_rented = True

    def return_vehicle(self):
        self.is_rented = False

    def __str__(self):
        status = "rented" if self.is_rented else "available"
        return f"{self.make} {self.model} ({self.plate}) [{status}]"


class Renter:
    def __init__(self, name, license_no):
        # Assign through the properties so initial values are validated too.
        self.name = name
        self.license_no = license_no
        self.rented = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a non-empty string.")
        self.__name = value

    @property
    def license_no(self):
        return self.__license_no

    @license_no.setter
    def license_no(self, value):
        if (isinstance(value, bool)
                or not isinstance(value, (int, float))
                or not value > 0):
            raise ValueError("Licence number must be a positive number.")
        self.__license_no = value


class ElectricCar(Vehicle):
    def __init__(self, make, model, plate, battery_kwh):
        super().__init__(make, model, plate)
        self.battery_kwh = battery_kwh

    def __str__(self):
        return f"Electric car: {super().__str__()} | battery: {self.battery_kwh} kWh"


class Motorbike(Vehicle):
    def __init__(self, make, model, plate, engine_cc):
        super().__init__(make, model, plate)
        self.engine_cc = engine_cc

    def __str__(self):
        return f"Motorbike: {super().__str__()} | engine: {self.engine_cc} cc"
