class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name.title()} serves {self.type} food.")

    def open_restaurant(self):
        print(f"{self.name.title()} is now open.")

new_restaurant = Restaurant('garden grille', 'vegetarian')
restaurant_2 = Restaurant('tortilla flats', 'mexican')
restaurant_3 = Restaurant('ivy tavern', 'pub')

print(new_restaurant.name.title())
print(new_restaurant.type)
new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()
restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()
restaurant_3.describe_restaurant()
restaurant_3.open_restaurant()