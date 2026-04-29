
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient in ingredients:
            if ingredients[ingredient] > self.machine_resources.get(ingredient, 0):
                print(f"Sorry, not enough {ingredient} to make sandwich.")
                return False

        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        for ingredient in order_ingredients:
            self.machine_resources[ingredient] -= order_ingredients[ingredient]

        print(f"Enjoy your {sandwich_size} sandwich.")