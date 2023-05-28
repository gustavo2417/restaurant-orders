import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.path = source_path
        self.dishes = set()
        self.new_list = []
        self.increase_menu()

    def read_file(self):
        with open(self.path, encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=",", quotechar='"')
            list_of_recipes = list(reader)

        return list_of_recipes

    def increase_ingredient(self, name, ingredient, amount):
        for index in self.new_list:
            if index.name == name:
                index.add_ingredient_dependency(ingredient, amount)

    def increase_menu(self):
        other_list = []

        for i in self.read_file():
            dish = Dish(i["dish"], float(i["price"]))
            ingredient = Ingredient(i["ingredient"])
            amount = int(i["recipe_amount"])
            if dish.name not in other_list:
                other_list.append(dish.name)
                dish.add_ingredient_dependency(ingredient, amount)
                self.new_list.append(dish)

            self.increase_ingredient(dish.name, ingredient, amount)

        for index in self.new_list:
            self.dishes.add(index)

        return self.dishes
