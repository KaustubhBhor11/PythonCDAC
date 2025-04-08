class AmountInvalidException(Exception):
    def __init__(self,msg="Amount is invalid"):
        super().__init__(msg)
        self.msg=msg