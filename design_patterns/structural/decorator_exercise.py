"""
PIZZERIA

Korzystając z wzorca projektowego Decorator stworzmy system pozwalający złożyć pizze o dowolnych kombinacjach
składników.
Do tego celu posłuż się podstawową strukturą dekoratora.
Chcemy aby podstawową klasą była klasa PlainPizza. Pizza posiada już swoją cenę. Każdy następny składnik powinien
zwiększać cenę pizzy.
*   Gotowa pizza za pomocą metody get_cost() zwraca docelowy koszt pizzy.
*   Gotowa pizza za pomocą metody get_description() zwraca string zawierający wszystkie składniki pizzy.

Przykładowo mamy do dyspozycji następujące składniki: Mozzarella, Ham, Mushrooms, Salami. KAŻDY SKLADNIK MA SWOJĄ CENĘ!

"""
from abc import ABC, abstractmethod


class Pizza(ABC):

    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_description(self):
        pass


class PlainPizza(Pizza):

    def __init__(self, cost):
        self._cost = cost
        self._description = "base of pizza"

    def get_cost(self):
        return self._cost

    def get_description(self):
        return self._description


class PizzaDecorator(Pizza):

    def __init__(self, plain: Pizza):
        self._wrappee = plain

    def get_cost(self):
        return self._wrappee.get_cost()

    def get_description(self):
        return self._wrappee.get_description()


class Mozzarella(PizzaDecorator):
    _COST = 2
    _DESCRIPTION = "mozzarella"

    def get_cost(self):
        return self._COST + super().get_cost()

    def get_description(self):
        return f"{self._DESCRIPTION}, {super().get_description()}"


class Ham(PizzaDecorator):
    _COST = 4
    _DESCRIPTION = "ham"

    def get_cost(self):
        return self._COST + super().get_cost()

    def get_description(self):
        return f"{self._DESCRIPTION}, {super().get_description()}"


class Mushrooms(PizzaDecorator):
    _COST = 3
    _DESCRIPTION = "mushrooms"

    def get_cost(self):
        return self._COST + super().get_cost()

    def get_description(self):
        return f"{self._DESCRIPTION}, {super().get_description()}"


class Salami(PizzaDecorator):
    _COST = 5
    _DESCRIPTION = "salami"

    def get_cost(self):
        return self._COST + super().get_cost()

    def get_description(self):
        return f"{self._DESCRIPTION}, {super().get_description()}"


if __name__ == '__main__':
    plain_pizza = PlainPizza(10)

    # ham pizza
    ham_pizza = Ham(plain_pizza)
    print(ham_pizza.get_cost())
    print(ham_pizza.get_description())

    # ham and mushroom pizza
    ham_mushroom_pizza = Mushrooms(ham_pizza)
    print(ham_mushroom_pizza.get_cost())
    print(ham_mushroom_pizza.get_description())
