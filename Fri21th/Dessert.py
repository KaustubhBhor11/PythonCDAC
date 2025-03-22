from abc import ABC ,abstractmethod
class Dessert(ABC):
    def __init__(self,name):
        self.name=name


    def name_of_item(self):
        return self.name

    @abstractmethod
    def cost_of_item(ABC):
        pass

class candy(Dessert):
    def __init__(self,weight,name):
        super().__init__(name)
        self.weight=weight
        self.price=(self.weight//1000)*50 # Rs.50/kg

    def cost_of_item(self):
        return self.price
    def __repr__(self):
        return f"{self.name} {self.price}"

class cookie(Dessert):
    def __init__(self,unit,name):
        super().__init__(name)
        self.unit=unit
        self.price=(self.unit//12)*10 # Rs.10/dozen

    def cost_of_item(self):
        print(self.price)
        return self.price
    def __repr__(self):
        return f"{self.name} {self.price}"

class icecream(Dessert):
    def __init__(self,unit,name):
        super().__init__(name)
        self.unit=unit
        self.price=(self.unit)*30# Rs.30/unit

    def cost_of_item(self):
        return self.price

    def __repr__(self):
        return f"{self.name} {self.price}"

class sundae(icecream):
    def __init__(self,unit,name):
        self.topping_name=name
        super().__init__(unit,"Icecream")
        self.price=super().price+2 #Rs 2 / gram

    def cost_of_item(self):
        return self.price

    def __repr__(self):
        return f"{self.name} {self.price}"

class checkout():
    def __init__(self):
        self.list_of_dessert=[]
        self.count=0
        self.total_price=0

    def add_dessert(self,dessert):
        self.list_of_dessert.append(dessert)
        self.count+=1
        self.total_price+=dessert.cost_of_item()

    def clear_cash_register(self):
        self.list_of_dessert.clear()
        self.count=0
    def total_items(self):
        return self.count
    def total_price(self):
        return self.total_price


    def print_invoice(self):
        for i in self.list_of_dessert:
            print(i)
        print(f"Totol Items :{self.count} \nTotal price :{self.total_price}")

class empty_cart_exception(Exception):
    def __init__(self,msg):
        self.msg=msg


dessert_name=input("Pleaes input desert name")
check_out = checkout()
if dessert_name.lower() == "candy":
    weight = int(input("Enter weight of candy "))
    # print(weight)
    candy1 = candy(weight,"Candy")
    # print(candy1.cost_of_item())
    check_out.add_dessert(candy1)
elif  dessert_name.lower() == "cookie":
    weight = int(input(f"Enter dozen of {dessert_name.lower()} "))
    cookie1 =  cookie(weight,"cookie")
    check_out.add_dessert(cookie1)
elif  dessert_name.lower() == "icecream":
    weight = int(input(f"Enter unit of {dessert_name.lower()} "))
    icecream =  icecream(weight,"icecream")
    check_out.add_dessert(icecream)
elif  dessert_name.lower() == "sundae":
    weight = int(input(f"Enter unit of {dessert_name.lower()} "))
    sundae1 =  sundae(weight,"sundae")
    check_out.add_dessert(sundae1)
else:
    print("Please enter valid input")
check_out.print_invoice()




