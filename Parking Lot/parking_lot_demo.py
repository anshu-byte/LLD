from parking_lot import ParkingLot
from level import Level
from car import Car
from motorcycle import Motorcycle
from truck import Truck


class ParkingLotDemo:

    @staticmethod
    def run():
        parking_lot = ParkingLot.get_instance()
        parking_lot.add_level(Level(1, 3))
        parking_lot.add_level(Level(2, 3))

        car = Car("ABC-1234")
        truck = Truck("DEF-5678")
        motorcycle = Motorcycle("GHI-9012")

        # Park Vehicles
        parking_lot.park_vehicle(car)
        parking_lot.park_vehicle(truck)
        parking_lot.park_vehicle(motorcycle)

        car = Car("JKL-3456")
        parking_lot.park_vehicle(car)

        # Display Availability
        parking_lot.display_availability()

        # Unpark Vehicles
        parking_lot.unpark_vehicle(car)

        print()

        # Display updated Availability
        parking_lot.display_availability()


if __name__ == "__main__":
    ParkingLotDemo.run()
