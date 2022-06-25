import random


class Investments:
    def __init__(self):
        self.number = None
        self.cash = None

    def buy(self, number):
        self.number = number
        return number

    def sell(self, number):
        self.number = number
        return number

    def upside(self):
        # self.to_buy(True)
        goodfood = Goodfood()
        sell = float(input("What price is attractive enough to start dumping shares? ––> "))
        upside = goodfood.current_shares * self.sell(sell)
        print(f"Selling for ${sell} will bank a total of ${upside} for a profit of ${(upside - goodfood.current_total())}")

class Goodfood(Investments):
    def __init__(self):
        super().__init__()
        self.current_shares = 250
        self.current_avg = 7.80

    def current_total(self):
        x = self.current_avg * self.current_shares
        return x


x = Investments()
x.upside()
