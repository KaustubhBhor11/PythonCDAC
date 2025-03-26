from abc import ABC , abstractmethod 
class DessertItem(ABC):
    def __init__(self,name):
        self.name=name

    def get_name(self):
        return self.name
    
    @abstractmethod
    def item_cost():
        pass