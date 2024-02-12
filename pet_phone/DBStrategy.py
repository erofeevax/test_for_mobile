from abc import ABC, abstractmethod
import pickle

class DBStrategy(ABC):

    @abstractmethod
    def dump(self):
        pass

    @abstractmethod
    def load(self):
        pass

class fileDBStrategy(DBStrategy):
    
    def dump(self, file, obj):
        with open(file, 'wb') as f:
            pickle.dump(obj, f)
    
    def load(self, file):
        with open(file, 'rb') as f:
            return pickle.load(f)
