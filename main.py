### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item in ingredients:
            if ingredients[item] >= self.machine_resources[item]:
                print(f"Sorry, not enough ingredients for {item}")
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input(how many quarters?: )"""
        print("Please enter coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))

        total = ((quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + pennies)

        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost:
            print(f"Sorry, not enough money for {cost}, money refunded")
            return False
        else:
            change = round(coins - cost, 2)
            if change > 0:
                print(f"TRANSACTION SUCCESFUL. \nhere is ${change} in change. Enjoy your {choice} sandwich")
            return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]

### Make an instance of SandwichMachine class and write the rest of the codes ###

machine = SandwichMachine(resources)

machine_on = True

while machine_on:
    choice = input("What would you like? (small/medium/large/off) ").lower()

    if choice == "off":
        machine_on = False
        print("Machine turning off.")

    elif choice in ["small", "medium", "large"]:
        order = recipes[choice]
        if machine.check_resources(order["ingredients"]):
            payment = machine.process_coins()
            if machine.transaction_result(payment, order["cost"]):
                machine.make_sandwich(choice, order["ingredients"])

    else:
        print("invalid option.")