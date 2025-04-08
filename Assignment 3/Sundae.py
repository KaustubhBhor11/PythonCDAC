from Icecream import Icecream
class Sundae(Icecream):

    def __init__(self,name,unit):
        super().__init__(name,unit)
        self.price=super().price + 10 

    def item_cost(self):
        return self.price
    
    def __repr__(self):
        return f"name {super().get_name()} price {self.price}"