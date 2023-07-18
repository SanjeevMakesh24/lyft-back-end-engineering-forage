from abc import ABC

from car import Car


class SternmanEngine(ABC):
    def __init__(self, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on

    def engine_should_be_serviced(self):
        if self.warning_light_is_on:
            return True
        else:
            return False

    def engine_type(self):
        return "Sternman Engine"