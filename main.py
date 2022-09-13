from pizza import Peperoni, BBQ

class Order():
    def __init__(self):
        self.items = []

    def add(self, pizza):
        self.items.append(pizza)

    def delete(self, pizza):
        self.items.remove(pizza)

    def print_bill(self):
        total = 0
        for pizza in self.items:
            print(pizza, pizza.calculate_price())
            total += pizza.calculate_price()
        print('-' * 20)
        print(f'Итого: {total} р.')





toping_reserves = {'base': 100, 'tomato': 50, 'beacon': 200, 'cheese': 60, 'sausage': 1, 'chili pepper': 40,
                         'chicken': 200, 'BBQ sause': 40, 'shrims': 100, 'mussels':200, 'squid':220, 'onion circles': 30, 'olives':70}


Sasha = Order()
Sasha.add(Peperoni())
Sasha.add(Peperoni())
Sasha.add(Peperoni())
Sasha.add(BBQ())

for pizza in Sasha.items.copy():
    if pizza.can_cook(toping_reserves):
        print(f'Ваша пицца {pizza} готова')
        pizza.make(toping_reserves)
    else:
        print(f'Мы не смогли приготовить пиццу {pizza}. Не хватает ингридиентов')
        Sasha.delete(pizza)
print('Ваш чек:')
Sasha.print_bill()
