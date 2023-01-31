from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_moneymachine=MoneyMachine()
my_coffeemaker=CoffeeMaker()
my_menu=Menu()
is_on= True


        
while is_on:
    options=my_menu.get_items()
    choice=input(f"What would you like? ({options}):")
    if choice=="off":
        is_on=False
    elif choice=="report":
        my_coffeemaker.report()
        my_moneymachine.report()
    else:
        drink=my_menu.find_order(choice)
        if my_coffeemaker.check_resources(drink):
            if my_moneymachine.make_payment(drink.cost):
                my_coffeemaker.make_coffee(drink)


   





