from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def hello(self):
        pass

    @staticmethod
    def print():
        print("Inb animal class")

class cat(Animal):
    def hello(self):
        print("Meeeooooo")


# c1=cat()
# c1.hello()


