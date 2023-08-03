
class Bar:
    def __init__(self):
        pass
        # self.bartab = 0

    def drink_sell(self, customer, room):
        if customer.wallet > 5:
            room.tab +=5
            customer.wallet -= 5
            return "Cha-ching"
        return "You're skint mate"
        
    