from DessertItem import DessertItem  
class Candy(DessertItem):

    def __init__(self,name,weight):
        super().__init__(name) 
        self.price=(float(weight)/1000)*50

    def item_cost(self):
        return self.price
    
    def __repr__(self):
        return f"name {super().get_name()} price {self.price}"