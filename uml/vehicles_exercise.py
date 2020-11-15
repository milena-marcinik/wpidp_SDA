"""
This module contains uml examples.
"""

from abc import ABC, abstractmethod
from typing import Type, Optional


class Vehicle(ABC):
    """This abstract class represents vehicle."""

    def __init__(self, model: str, brand: str):
        self.model = model
        self.brand = brand

    @abstractmethod
    def is_dirty(self) -> bool:
        pass

    @abstractmethod
    def drive(self) -> bool:
        pass


class Car(Vehicle):
    """This class represents car."""

    def __init__(self, model: str, brand: str, number_of_seats: int):
        super().__init__(model, brand)
        self.number_of_seats = number_of_seats

    def is_dirty(self) -> bool:
        pass

    def drive(self) -> bool:
        pass

    def drive_on_holidays(self):
        pass


class Truck(Vehicle):
    """This class represents truck."""

    def __init__(self, model: str, brand: str, load: float):
        super().__init__(model, brand)
        self._load = load

    def is_dirty(self) -> bool:
        pass

    def drive(self) -> bool:
        pass

    def deliver_cargo(self):
        pass


class CarWash:
    """This class represents car wash."""

    def __init__(self, price_list: str):
        self.price_list = price_list

    def wash_vehicle(self, vehicle: Vehicle):
        pass

    def is_out_of_order(self) -> bool:
        pass


class Owner:
    """This class represents owner."""

    def __init__(self):
        self._vehicle: Optional[Vehicle] = None  # poczatkowo owner nie ma zadnego vehicle

    def go_to_car_wash(self, car_wash: CarWash):
        car_wash.wash_vehicle(self._vehicle)  # to nie jest odczytane z uml, tylko mozna sie tego domyslic

    def buy_new_vehicle(self, vehicle_type: Type[Vehicle]):
        pass


if __name__ == '__main__':
    car_wash1 = CarWash('this is price list')
    car_wash2 = CarWash('this is price list')

    owner = Owner()
    owner.buy_new_vehicle(Car)
    owner.buy_new_vehicle(Truck)

    owner.go_to_car_wash(car_wash1)
    owner.go_to_car_wash(car_wash2)

