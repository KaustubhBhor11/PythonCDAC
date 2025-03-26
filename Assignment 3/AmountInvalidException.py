class AmountInvalidException(Exception):
    def __init__(self,msg="Amount is invalid"):
        self.msg=msg