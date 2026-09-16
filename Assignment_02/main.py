"""Run with python main.py to demonstrate the assignment requirements."""

from rental import ElectricCar, Motorbike, Renter, Vehicle


def main():
    car = Vehicle("Toyota", "Yaris", "1AB234")
    electric_car = ElectricCar("BYD", "Dolphin", "2CD567", 44.9)
    motorbike = Motorbike("Honda", "Wave", "3EF890", 110)
    renter = Renter("Theikdi Nyan", 12345)

    print("Renter:", renter.name, "| licence:", renter.license_no)
    print("Initially rented vehicles:", renter.rented)

    print("\nRenting and returning:")
    print("Before:", car)
    car.rent()
    renter.rented.append(car)
    print("After renting:", car)
    print("Renter's vehicle count:", len(renter.rented))
    car.return_vehicle()
    renter.rented.remove(car)
    print("After returning:", car)
    print("Renter's vehicle count:", len(renter.rented))

    print("\nInvalid renter creation:")
    for name, license_no in [("", 12345), ("Example", 0), ("Example", -1)]:
        try:
            Renter(name, license_no)
        except ValueError as error:
            print("Caught ValueError:", error)

    print("\nInvalid changes to an existing renter:")
    try:
        renter.name = ""
    except ValueError as error:
        print("Caught ValueError:", error)
    try:
        renter.license_no = 0
    except ValueError as error:
        print("Caught ValueError:", error)
    print("Valid details preserved:", renter.name, renter.license_no)

    print("\nPolymorphism: one list, three string formats:")
    vehicles = [car, electric_car, motorbike]
    for vehicle in vehicles:
        print(vehicle)

    print("\nSubclasses inherit rental behavior:")
    for vehicle in [electric_car, motorbike]:
        print("Is a Vehicle:", isinstance(vehicle, Vehicle))
        vehicle.rent()
        print(vehicle)
        vehicle.return_vehicle()
        print(vehicle)


if __name__ == "__main__":
    main()
