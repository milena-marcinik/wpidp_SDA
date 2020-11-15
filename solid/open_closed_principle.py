from abc import ABC, abstractmethod


class Discount(ABC):

    @abstractmethod
    def get_discount(self):
        pass


class EasterDiscount(Discount):
    _EASTER_DISCOUNT = '30%'

    def get_discount(self):
        return f'{self._EASTER_DISCOUNT} on Easter'


class BlackFridayDiscount(Discount):
    _BLACK_FRIDAY_DISCOUNT = '50%'

    def get_discount(self):
        return f'{self._BLACK_FRIDAY_DISCOUNT} on Black Friday'


class BackToSchoolDiscount(Discount):
    _DISCOUNT = "29%"

    def get_discount(self):
        return f'{self._DISCOUNT} on Back To School'


class DiscountManager:

    def process_discount(self, discount: Discount):
        pass


discount_manager = DiscountManager()
# przekazujemy tutaj klase, lepiej jednak dzialac na obiektach (bylo Type: Discount)
# discount_manager.process_discount(EasterDiscount)
discount_manager.process_discount(EasterDiscount())  # tutaj juz na obiektach
discount_manager.process_discount(BlackFridayDiscount())
discount_manager.process_discount(BackToSchoolDiscount())


EasterDiscount().get_discount()
BackToSchoolDiscount().get_discount()
BlackFridayDiscount().get_discount()
