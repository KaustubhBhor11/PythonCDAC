
class CartIsEmptyException(Exception):
    def __init__(self,msg="Cart is empty, please add items"):
        super().__init__(msg)
        self.msg=msg
