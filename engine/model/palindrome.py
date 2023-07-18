from datetime import datetime

from engine.sternman_engine import SternmanEngine
from car import Car
from engine.battery.spindler_battery import SpindlerBattery

class Palindrome(SternmanEngine, Car, SpindlerBattery):

    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage, warning_light_is_on):
        super().__init__(warning_light_is_on)
        Car.__init__(self, current_date, last_service_date, current_mileage, last_service_mileage)
        SpindlerBattery.__init__(self, current_date, last_service_date)

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
