import DessertItem
class Cookie(DessertItem):

    def __init__(self,name,unit):
        super(name)
        self.price=(unit/12)*40

    def item_cost(self):
        return self.price