budget = 0
share_buy_value = 0
fixed_share_percent = 75
shares_number = 0
price = 0
payed_provision = 0
provision_percent = 0.3
drop_price_percent = 3

while True:

    budget = input("Podaj wartość budżetu w zł: ").strip()

    while True:

        number_test = budget.isdecimal()

        if number_test is False:
            budget = input(
                "Wprowadzona wartość musi być liczbą, podaj raz jeszcze: ")
        else:
            break

    shares_number = input("Podaj ilość kupionych akcji: ").strip()

    while True:

        number_test = shares_number.isdecimal()

        if number_test is False:
            shares_number = input(
                "Wprowadzona wartość musi być liczbą, podaj raz jeszcze: ")
        else:
            break

    price = input("Podaj kurs akcji: ").strip()

    while True:

        number_test = price.isdecimal()

        if number_test is False:
            price = input(
                "Wprowadzona wartość musi być liczbą, podaj raz jeszcze: ")
        else:
            break

    payed_provision = input("Podaj zapłaconą prowizję: ").strip()

    while True:

        number_test = payed_provision.isdecimal()

        if number_test is False:
            payed_provision = input(
                "Wprowadzona wartość musi być liczbą, podaj raz jeszcze: ")
        else:
            break

    share_buy_value = int(shares_number)*int(price)+int(payed_provision)

    budget_use = int(share_buy_value) / int(budget) * 100

    sell_value = int(share_buy_value) - (int(budget)
                                         * int(fixed_share_percent)/100)
    share_value = ((int(price)*int(shares_number)) +
                   int(payed_provision))/int(shares_number)

    share_sell_number = sell_value/share_value

    budget_not_used = int(budget) - share_buy_value

    buy_value = (1-(drop_price_percent/100)) * share_value

    buy_number = budget_not_used / (buy_value * ((provision_percent/100)+1))

    buy_values = buy_value * buy_number

    if int(share_buy_value) > int(budget):
        print(
            f"Wykorzystanie budżetu wynosi {round(budget_use, 2)}% Ponadto "
            "wartość zakupionych akcji jest większa od budżetu o "
            f"{int(share_buy_value)-int(budget)} zł!!! "
            f"Należy pozbyć się {round(share_sell_number)} akcji o wartości "
            f"{sell_value} zł!! aby zejść do progu bezpieczeństwa")
    if budget_use < 75:
        print(f"Wykorzystanie budżetu wynosi {round(budget_use, 2)}%"
              f" Można jeszcze kupić {round(buy_number)} "
              f"akcji o wartości {round(buy_values, 2)} zł")
