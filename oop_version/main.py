from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()

is_on = True


money  = MoneyMachine()
coffeemachine = CoffeeMaker()


my_money_machine = MoneyMachine()


while is_on:
    options = menu.get_items()
    choice = input(f"what would you like to have today ({options}):").lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffeemachine.report()
        my_money_machine.report()
    elif choice == "refill":
        coffeemachine.refill()
    else:
        drink = menu.find_drink(choice)
        if coffeemachine.is_resource_sufficient(drink):
            if (money.make_payment(drink.cost)):
                coffeemachine.make_coffee(drink)





            
                 
        
        


         
      
