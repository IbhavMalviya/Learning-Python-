class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        # Print the restaurant name
        print(f"The restaurant name is {self.restaurant_name}")
        # Print the cuisine type
        print(f"The cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        # Print that the restaurant is open
        print("The restaurant is open now")


kfc = Restaurant("KFC", "Fastfood")
thai = Restaurant("Thai", "Spicy")
chinese = Restaurant("Chinese", "Hot")

kfc.describe_restaurant()
kfc.open_restaurant()
thai.describe_restaurant()
thai.open_restaurant()
chinese.describe_restaurant()
chinese.open_restaurant()

class IceCream(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavour = "chocolate"

    def ice_cream_flavour(self):
        # Print the flavor of the ice cream
        print(f"The flavor of ice cream is {self.flavour}")


ice_cream_stand = IceCream("Amul", "Dessert", "chocolate")
ice_cream_stand.describe_restaurant()
ice_cream_stand.open_restaurant()
ice_cream_stand.ice_cream_flavour()