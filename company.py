class Company_next_move():
    """Creating company move"""

    def __init__(self, first_buy_value, first_buy_pcs,
                 first_buy_provision, buy_pack_value):
        """Initialization of atributes"""
        self.first_buy_value = first_buy_value
        self.first_buy_pcs = first_buy_pcs
        self.first_buy_provision = first_buy_provision
        self.buy_pack = buy_pack_value

    def next_buy(self, drop_percentages=0):
        """Calculation of next buy value acording first buy value"""
        next_buy_value = self.first_buy_value * (1 - (drop_percentages/100))
        print(next_buy_value)
