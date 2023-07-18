from abc import ABC, abstractmethod

class Tire(ABC):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    @abstractmethod
    def tire_should_be_serviced(self):
        pass
