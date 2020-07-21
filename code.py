# resources available
water = 400
milk = 540
coffee_beans = 120
disposable_cups = 9
money = 550

# for one espresso
esp_water = 250
esp_coffee_beans = 16
esp_money = 4

# for one latte
lat_water = 350
lat_milk = 75
lat_coffee_beans = 20
lat_money = 7

# for one cappuccino
cap_water = 200
cap_milk = 100
cap_coffee_beans = 12
cap_money = 6


def take_action():
    while True:
        user_action = input("Write action (buy, fill, take, remaining, exit):")
        if user_action == "remaining":
            def remaining_resources():
                print("The coffee machine has:")
                print(water, "of water")
                print(milk, "of milk")
                print(coffee_beans, "of coffee beans")
                print(disposable_cups, "of disposable cups")
                print("$" + str(money), "of money")
                return

            remaining_resources()

        if user_action == "exit":
            break

        if user_action == "buy":
            def buy_coffee():
                global water
                global milk
                global coffee_beans
                global disposable_cups
                global money
                coffee_flavour = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to "
                                       "main "
                                       "menu:")
                

                if coffee_flavour == "1":
                    if min(water // esp_water, milk // milk, coffee_beans // esp_coffee_beans,
                           disposable_cups // disposable_cups) >= 1:
                        print("I have enough resources, making you a coffee!")
                        water -= esp_water
                        milk -= 0
                        coffee_beans -= esp_coffee_beans
                        disposable_cups -= 1
                        money += esp_money
                        return
                    else:
                        if water < esp_water:
                            print("Sorry, not enough water!")
                        elif milk < milk:
                            print("Sorry, not enough milk!")
                        elif coffee_beans < esp_coffee_beans:
                            print("Sorry, not enough coffee beans!")
                        else:
                            print("Sorry, not enough disposable cups")
                        return

                elif coffee_flavour == "2":
                    if min(water // lat_water, milk // lat_milk, coffee_beans // lat_coffee_beans,
                           disposable_cups // disposable_cups) >= 1:
                        print("I have enough resources, making you a coffee!")
                        water -= lat_water
                        milk -= lat_milk
                        coffee_beans -= lat_coffee_beans
                        disposable_cups -= 1
                        money += lat_money
                        return
                    else:
                        if water < lat_water:
                            print("Sorry, not enough water!")
                        elif milk < lat_milk:
                            print("Sorry, not enough milk!")
                        elif coffee_beans < lat_coffee_beans:
                            print("Sorry, not enough coffee beans!")
                        else:
                            print("Sorry, not enough disposable cups")
                        return

                elif coffee_flavour == "3":
                    if min(water // cap_water, milk // cap_milk, coffee_beans // cap_coffee_beans,
                           disposable_cups // disposable_cups) >= 1:
                        print("I have enough resources, making you a coffee!")
                        water -= cap_water
                        milk -= cap_milk
                        coffee_beans -= cap_coffee_beans
                        disposable_cups -= 1
                        money += cap_money
                        return
                    else:
                        if water < cap_water:
                            print("Sorry, not enough water!")
                        elif milk < cap_milk:
                            print("Sorry, not enough milk!")
                        elif coffee_beans < cap_coffee_beans:
                            print("Sorry, not enough coffee beans!")
                        else:
                            print("Sorry, not enough disposable cups")
                        return

            buy_coffee()

        if user_action == "fill":
            def fill_container():
                global water
                global milk
                global coffee_beans
                global disposable_cups
                global money
                add_water = input("Write how many ml of water do you want to add:")
                add_milk = input("Write how many ml of milk do you want to add:")
                add_coffee_beans = input("Write how many grams of coffee beans do you want to add:")
                add_disposable_cups = input("Write how many disposable cups do you want to add:")

                water += int(add_water)
                milk += int(add_milk)
                coffee_beans += int(add_coffee_beans)
                disposable_cups += int(add_disposable_cups)
                money += 0
                return

            fill_container()

        if user_action == "take":
            def take_money():
                global water
                global milk
                global coffee_beans
                global disposable_cups
                global money
                print("I gave you " + "$" + str(money))
                water -= 0
                milk -= 0
                coffee_beans -= 0
                disposable_cups -= 0
                money -= money
                return

            take_money()


take_action()
