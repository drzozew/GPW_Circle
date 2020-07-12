from wallets import Wallet

wallets = []
x = 0

while x < 2:

    add_wallet = {
        'name': input("Podaj nazwę portfela: "),
        'currency': input("Podaj walutę portfela: "),
        'value': input("Podaj wartość porftela: ")
    }
    wallets.append(add_wallet)
    x = x + 1

wallet_1 = wallets[0]
wallet_2 = wallets[1]

z = Wallet(wallet_1['name'], wallet_1['currency'], int(wallet_1['value']))
z.show_value()
y = Wallet(wallet_2['name'], wallet_2['currency'], int(wallet_2['value']))
y.show_value()
