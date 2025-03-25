class Demo():
    def __init__(self):
        self.first=1
        self.__second=2

    def __lets_print(self):
        print("lets print")


d1=Demo()
print(d1.first)
print(d1._Demo__second)
print(d1._Demo__lets_print())

