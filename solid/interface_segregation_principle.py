from abc import ABC, abstractmethod


class ProductActionsInterface(ABC):

    @abstractmethod
    def show_reviews(self):
        pass


class ComputerActionInterface(ProductActionsInterface, ABC):

    @abstractmethod
    def find_in_outlet(self):
        pass


class SoftwareActionInterface(ProductActionsInterface, ABC):

    @abstractmethod
    def try_for_seven_days(self):
        pass


class ComputerActionsUI(ComputerActionInterface):

    def find_in_outlet(self):
        pass

    def show_reviews(self):
        pass


class SoftwareActionsUI(SoftwareActionInterface):
    def try_for_seven_days(self):
        pass

    def show_reviews(self):
        pass


ComputerActionsUI().find_in_outlet()
SoftwareActionsUI().try_for_seven_days()
