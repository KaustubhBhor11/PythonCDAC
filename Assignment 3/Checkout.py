import CartIsEmptyException

class Checkout:
    def __init__(self):
        self.cashRegister=[]
        self.itemcount=0
        self.total_price=0

    def add_dessert(self,my_dessert):
        self.cashRegister.append(my_dessert)
        self.itemcount+=1
        self.total_price+=my_dessert.item_cost()
        return self.cashRegister
    
    def clear_cash_register(self):
        try:
            self.cashRegister.clear()
            raise CartIsEmptyException
        except CartIsEmptyException as e :
            print(e)

    def get_item_count(self):
        return self.itemcount
    
    def get_item_total(self):
        return self.total_price
    
    def get_invoice(self):
        for i in self.cashRegister:
            print(i.name,i.item_cost)
        

