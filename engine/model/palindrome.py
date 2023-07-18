from datetime import datetime

from engine.sternman_engine import SternmanEngine
from car import Car
from engine.battery.spindler_battery import SpindlerBattery
from engine.tires.octoprime_tire import OctoprimeTire

class Palindrome(SternmanEngine, Car, SpindlerBattery, OctoprimeTire):

    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage, warning_light_is_on, tire):
        super().__init__(warning_light_is_on)
        Car.__init__(self, current_date, last_service_date, current_mileage, last_service_mileage, tire)
        SpindlerBattery.__init__(self, current_date, last_service_date)
        #New Criteria - Octoprime Tire
        OctoprimeTire.__init__(self, tire)

    def needs_service(self):
        if self.battery_should_be_serviced() or self.engine_should_be_serviced() or self.tire_should_be_serviced():
            return True
        else:
            return False
