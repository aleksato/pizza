class Pizza:
    def __init__(self, diam):
        self.diam = diam
        self.ingredients = ['base']

    def calculate_price(self):
        toping_prices = {'base': 100, 'tomato': 50, 'beacon': 200, 'cheese': 60, 'sausage': 200, 'chili pepper': 40,
                         'chicken': 200, 'BBQ sause': 40}
        total_pr = 0
        for ingredient in self.ingredients:
            total_pr += toping_prices[ingredient]
        return total_pr

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)


class Peperoni(Pizza):
    def __init__(self, size=22):
        super().__init__(size)
        self.add_ingredient('chili pepper')
        self.add_ingredient('tomato')
        self.add_ingredient('cheese')
        self.add_ingredient('sausage')


class BBQ(Pizza):
    def __init__(self, size=22):
        super().__init__(size)
        self.add_ingredient('chicken')
        self.add_ingredient('BBQ sause')
        self.add_ingredient('cheese')


peperony = Peperoni()
bbq = BBQ()


print(f'итого с вас: {bbq.calculate_price()}')
print(bbq.ingredients)
