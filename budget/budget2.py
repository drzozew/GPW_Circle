budget = 0
share_buy_value = 0


budget = int(input("Podaj wartość budżetu w zł: ").strip())
share_buy_value = int(input("Podaj wartoś zakupu akcji w zł: ").strip())


budget_use = share_buy_value / budget * 100

print(f"Wykorzystanie budżetu wynosi {round(budget_use, 2)}%")
