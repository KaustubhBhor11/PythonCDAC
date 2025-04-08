from DessertItem import DessertItem  
class Icecream(DessertItem):

    def __init__(self,name,unit):
        super().__init__(name) 
        self.price=(int(unit))*40

    def item_cost(self):
        return self.price
    
    def __repr__(self):
        return f"name {super().get_name()} price {self.price}"