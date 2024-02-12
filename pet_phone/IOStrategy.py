from abc import ABC, abstractmethod

class IOStrategy(ABC):
    @abstractmethod
    def input(self):
        pass
    def output(self):
        pass

class CliIOStrategy(IOStrategy):
    def input(self, text):
        return input(text)
    
    def output(self, text):
        print(text)
