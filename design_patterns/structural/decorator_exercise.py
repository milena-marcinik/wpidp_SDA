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
