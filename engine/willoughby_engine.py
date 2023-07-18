from abc import ABC

from car import Car


class WilloughbyEngine(ABC):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def engine_should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage > 60000

    def engine_type(self):
        return "Willoughby Engine"