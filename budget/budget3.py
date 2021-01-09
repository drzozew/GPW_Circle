budget = 0
share_buy_value = 0

while True:

    budget = input("Podaj wartość budżetu w zł: ").strip()

    while True:

        number_test = budget.isdecimal()

        if number_test is False:
            budget = input(
                "Wprowadzona wartość musi być liczbą, podaj raz jeszcze: ")
        else:
            break

    share_buy_value = input("Podaj wartoś zakupu akcji w zł: ").strip()

    while True:

        number_test = share_buy_value.isdecimal()

        if number_test is False:
            share_buy_value = input(
                "Wprowadzona wartość musi być liczbą, podaj raz jeszcze: ")
        else:
            break

    budget_use = int(share_buy_value) / int(budget) * 100

    print(f"Wykorzystanie budżetu wynosi {round(budget_use, 2)}%")
