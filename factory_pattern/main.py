import logging
from abc import ABC, abstractmethod
from typing import Union

# Налаштування логування
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)


# Абстрактний базовий клас для транспортних засобів
class Vehicle(ABC):
    def __init__(self, make: str, model: str, spec: str) -> None:
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self) -> None:
        pass

# Реалізація класу Car
class Car(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} ({self.spec} Spec): Двигун запущено")


# Реалізація класу Motorcycle
class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} ({self.spec} Spec): Мотор заведено")


# Абстрактний клас фабрики
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        pass


# Фабрика для транспортних засобів USA
class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "US")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "US")


# Фабрика для транспортних засобів EU
class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "EU")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "EU")


def create_and_start_vehicle(
    factory: VehicleFactory, vehicle_type: str, make: str, model: str
) -> None:
    if vehicle_type == "car":
        vehicle: Union[Car, Motorcycle] = factory.create_car(make, model)
    elif vehicle_type == "motorcycle":
        vehicle = factory.create_motorcycle(make, model)
    else:
        raise ValueError("Невідомий тип транспортного засобу")
    vehicle.start_engine()


if __name__ == "__main__":
    logger.info("US Vehicles:")
    us_factory = USVehicleFactory()
    create_and_start_vehicle(us_factory, "car", "Ford", "Mustang")
    create_and_start_vehicle(us_factory, "motorcycle", "Harley-Davidson", "Sportster")

    logger.info("\nEU Vehicles:")
    eu_factory = EUVehicleFactory()
    create_and_start_vehicle(eu_factory, "car", "Audi", "A4 AllRoad")
    create_and_start_vehicle(eu_factory, "motorcycle", "Ventus", "VT-200")
