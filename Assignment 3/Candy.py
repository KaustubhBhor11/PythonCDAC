import DessertItem
class Candy(DessertItem):

    def __init__(self,name,weight):
        super(name)
        self.price=(weight/1000)*50

    def item_cost(self):
        return self.price