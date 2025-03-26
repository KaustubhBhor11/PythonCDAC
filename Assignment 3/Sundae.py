import Icecream
class Sundae(Icecream):

    def __init__(self,name,unit):
        super(name,unit)
        self.price=super().price + 10 

    def item_cost(self):
        return self.price