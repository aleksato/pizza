class Pizza:
    def __init__(self, diam):
        self.diam = diam
        self.ingredients = ['base']

    def can_cook(self, reserves):
        for ingredient in self.ingredients:
            if reserves[ingredient] < 1:
                return False
        return True

    def make(self, reserves):
        for ingredient in self.ingredients:
            reserves[ingredient] -= 1

    def __repr__(self):
        return self.name



    def calculate_price(self):
        toping_prices = {'base': 100, 'tomato': 50, 'beacon': 200, 'cheese': 60, 'sausage': 200, 'chili pepper': 40,
                         'chicken': 200, 'BBQ sause': 40, 'shrims': 100, 'mussels':200, 'squid':220, 'onion circles': 30, 'olives':70}
        total_pr = 0
        for ingredient in self.ingredients:
            total_pr += toping_prices[ingredient]
        return total_pr

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)


class Peperoni(Pizza):
    def __init__(self, size=22):
        super().__init__(size)
        self.name = 'Пицца "Пеперони"'
        self.add_ingredient('chili pepper')
        self.add_ingredient('tomato')
        self.add_ingredient('cheese')
        self.add_ingredient('sausage')


class BBQ(Pizza):
    def __init__(self, size=22):
        super().__init__(size)
        self.name = 'Пицца "Барбекю"'
        self.add_ingredient('chicken')
        self.add_ingredient('BBQ sause')
        self.add_ingredient('cheese')

class SeaPizza(Pizza):
    def __init__(self,size=22):
        super().__init__(size)
        self.name = 'Пицца "Дары Моря"'
        self.add_ingredient('shrims')
        self.add_ingredient('mussels')
        self.add_ingredient('squid')
        self.add_ingredient('onion circles')
        self.add_ingredient('olives')




