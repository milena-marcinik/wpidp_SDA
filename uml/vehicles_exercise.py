"""
This module contains uml examples.
"""

from abc import ABC, abstractmethod
from typing import Type


class Vehicle(ABC):
    """This abstract class represents vehicle."""

    def __init__(self, model: str, brand: str):
        self.model = model
        self.brand = brand
        super().__init__()

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

    def __init__(self, vehicle: Vehicle):
        self._vehicle = vehicle

    def go_to_car_wash(self, car_wash: CarWash):
        pass

    def buy_new_vehicle(self, vehicle_type: Type[Vehicle]):
        pass
