class Company_next_move():
    """Creating company move"""

    def __init__(self, first_buy_value_in_grosze, first_buy_pcs,
                 first_buy_provision_in_grosze, buy_pack_value_in_grosze):
        """Initialization of atributes"""
        self.first_buy_value_in_grosze = first_buy_value_in_grosze
        self.first_buy_pcs = first_buy_pcs
        self.first_buy_provision_in_grosze = first_buy_provision_in_grosze
        self.buy_pack_in_grosze = buy_pack_value_in_grosze

    def next_buy(self, drop_percentages=0):
        """Calculation of next buy value acording first buy value"""
        next_buy_value = (self.first_buy_value_in_grosze *
                          (1 - (drop_percentages/100)))/100
        print(
            f"Kurs po jakim powinienem kupić kolejny pakiet to: "
            f"{round(next_buy_value, 2)}")

    def sell_set(self, up_percentages=0):
        """Calculation of sell value"""
        value_set = ((self.first_buy_value_in_grosze +
                      self.first_buy_provision_in_grosze) *
                     (1 + (up_percentages / 100)))/100
        print(f"Ustawić kurs sprzedaży na {round(value_set, 2)}")
