from datetime import datetime
from car import Car
from engine.willoughby_engine import WilloughbyEngine
from engine.battery.spindler_battery import SpindlerBattery


class Glissade(WilloughbyEngine, Car, SpindlerBattery):

    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        super().__init__(current_mileage, last_service_mileage)
        Car.__init__(self, current_date, last_service_date, current_mileage, last_service_mileage)
        SpindlerBattery.__init__(self, current_date, last_service_date)
    def needs_service(self):
        if self.battery_should_be_serviced() or self.engine_should_be_serviced():
            return True
        else:
            return False
