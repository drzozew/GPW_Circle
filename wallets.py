class Wallet():
    """Creating place to hold cash"""

    def __init__(self, name, currency, value_in_gr):
        """Initialization arguments"""
        self.name = name
        self.currency = currency
        self.value_in_gr = value_in_gr

    def show_value(self):
        print(f"W {self.name} jest {self.value_in_gr} {self.currency}")
