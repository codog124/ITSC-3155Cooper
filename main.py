import data
import sandwich_maker
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()

def main():
    ###  write the rest of the codes ###
    is_running = True

    while is_running:
        choice = input("What size sandwich?: (small [1.75] / medium [3.25] / large [5.50] / off): ").lower()

        if choice == "off":
            is_running = False

        elif choice in recipes:
            sandwich = recipes[choice]
            ingredients = sandwich["ingredients"]
            cost = sandwich["cost"]

            if sandwich_maker_instance.check_resources(ingredients):

                coins = cashier_instance.process_coins()

                if cashier_instance.transaction_result(coins, cost):
                    sandwich_maker_instance.make_sandwich(choice, ingredients)


if __name__=="__main__":
    main()
