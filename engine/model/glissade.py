from datetime import datetime
from car import Car
from engine.willoughby_engine import WilloughbyEngine
from engine.battery.spindler_battery import SpindlerBattery
from engine.tires.octoprime_tire import OctoprimeTire


class Glissade(WilloughbyEngine, Car, SpindlerBattery, OctoprimeTire):

    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage, tire):
        super().__init__(current_mileage, last_service_mileage)
        Car.__init__(self, current_date, last_service_date, current_mileage, last_service_mileage, tire)
        SpindlerBattery.__init__(self, current_date, last_service_date)
        #New Criteria - Octoprime Tire
        OctoprimeTire.__init__(self, tire)

    def needs_service(self):
        if self.battery_should_be_serviced() or self.engine_should_be_serviced() or self.tire_should_be_serviced():
            return True
        else:
            return False
