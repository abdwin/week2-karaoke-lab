
class Bar:
    def __init__(self, drink_price):
        self.drink_price = drink_price
        # self.bartab = 0

    def drink_sell(self, customer, room):
        if customer.wallet > self.drink_price:
            room.tab += self.drink_price
            customer.wallet -= self.drink_price
            return "Cha-ching"
        return "You're skint mate"
        
    