class CoffeeMachine:

    def __init__(self):
        self.money = 550
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9

    def ft_actions(self, action):
        if action == "buy":
            self.ft_buy()
        if action == "fill":
            self.ft_fill()
        if action == "take":
            self.ft_take()
        if action == "remaining":
            self.ft_coffee_machine_state()
        if action == "exit":
            return 0

    def ft_buy(self):
        print("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, "
              "back - to main menu:")
        coffee_variety = input()
        if coffee_variety == 'back':
            return 1
        else:
            coffee_variety = int(coffee_variety)
        if coffee_variety == 1:
            if self.water < 250:
                print("Sorry, not enough water!")
                return 0
            elif self.beans < 16:
                print("Sorry, not enough beans!")
                return 0
            elif self.cups < 1:
                return 0
            self.water -= 250
            self.beans -= 16
            self.money += 4
        if coffee_variety == 2:
            if self.water < 350:
                print("Sorry, not enough water!")
                return 0
            elif self.milk < 75:
                print("Sorry, not enough milk!")
                return 0
            elif self.beans < 20:
                print("Sorry, not enough beans!")
                return 0
            elif self.cups < 1:
                return 0
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.money += 7
        if coffee_variety == 3:
            if self.water < 200:
                print("Sorry, not enough water!")
                return 0
            elif self.milk < 100:
                print("Sorry, not enough milk!")
                return 0
            elif self.beans < 12:
                print("Sorry, not enough beans!")
                return 0
            elif self.cups < 1:
                return 0
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.money += 6
        self.cups -= 1
        print("I have enough resources, making you a coffee!")

    def ft_fill(self):
        print("Write how many ml of water do you want to add:")
        self.water += int(input())
        print("Write how many ml of milk do you want to add:")
        self.milk += int(input())
        print("Write how many grams of coffee beans do you want to add:")
        self.beans += int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        self.cups += int(input())

    def ft_take(self):
        print("I gave you $" + str(self.money))
        self.money -= self.money

    def ft_coffee_machine_state(self):
        print("\nThe coffee machine has:")
        print(str(self.water) + " of water")
        print(str(self.milk) + " of milk")
        print(str(self.beans) + " of coffee beans")
        print(str(self.cups) + " of disposable cups")
        print("$" + str(self.money) + " of money")

    def start(self):
        while True:
            print("\nWrite action (buy, fill, take, remaining, exit): ")
            action = input()
            if self.ft_actions(action) == 0:
                break


order = CoffeeMachine()
order.start()
