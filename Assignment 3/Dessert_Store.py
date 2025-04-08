from Cookie import Cookie
from Checkout import Checkout
from Candy import Candy
from Icecream import Icecream
from Sundae import Sundae
from CartIsEmptyException import CartIsEmptyException
from AmountInvalidException import AmountInvalidException
if __name__ == "__main__":
    checkout=Checkout()
    while 1 :
        print("""
            Choose operation to perform
            1. Add Dessert to cart
            2. Get Numbers of items
            3. Get total cost of items
            4. Get invoice
            5. Clear cashRegister
            6. Exit the store
        """)
        operation=input()
        if operation == '1' :
            try:
                my_dessert=input("Please enter the Desert name - Cookie,Candy,Icecream,Sundae \n")
                if my_dessert.lower() == 'cookie':
                    unit=input("Please enter units \n")
                    if int(unit) < 0:
                        raise AmountInvalidException("Invalid amount")
                    cookie1=Cookie(my_dessert,unit)
                    checkout.add_dessert(cookie1)
                    print("Cookie is added to basket\n")
                elif my_dessert.lower() == 'candy':
                    weight=input("Please enter weight\n")
                    if int(weight) < 0:
                        raise AmountInvalidException("Invalid amount")
                    Candy1=Candy(my_dessert,weight)
                    checkout.add_dessert(Candy1)
                    print("Candy is added to basket\n")
                elif my_dessert.lower() == 'icecream':
                    unit=input("Please enter unit\n")
                    if int(unit) < 0:
                        raise AmountInvalidException("Invalid amount")                    
                    icecream1=Icecream(my_dessert,unit)
                    checkout.add_dessert(icecream1)
                    print("Icecream is added to basket\n")
                elif my_dessert.lower() == 'sundae':
                    unit=input("Please enter unit\n")
                    if int(unit) < 0:
                        raise AmountInvalidException("Invalid amount")
                    Sundae1=Sundae(my_dessert,unit)
                    checkout.add_dessert(Sundae1)
                    print("Sundae is added to basket\n")
                else:
                    print("Please enter valid dessert\n")

            except ValueError as e :
                print("Please enter valid number")
            except AmountInvalidException as e :
                print("please enter valid Amount")
        
        elif operation == '2':
            print("Total Numbers of items",checkout.get_item_count())
        elif operation == '3':
            print("Total cost of items",checkout.get_item_total())
        elif operation == '4':
            checkout.get_invoice()
        elif operation == '5':
            checkout.clear_cash_register()
        elif operation == '6':
            print("Thank you for visiting store")
            break


        
    