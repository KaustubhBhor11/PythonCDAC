class CartIsEmptyException(Exception):
    def __init__(self,msg="Cart is empty"):
        self.msg=msg
