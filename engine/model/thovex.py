from datetime import datetime
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.battery.nubbin_battery import NubbinBattery

class Thovex(CapuletEngine, Car, NubbinBattery):

    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        super().__init__(current_mileage, last_service_mileage)
        Car.__init__(self, current_date, last_service_date, current_mileage, last_service_mileage)
        NubbinBattery.__init__(self, current_date, last_service_date)
    def needs_service(self):
        if self.battery_should_be_serviced() or self.engine_should_be_serviced():
            return True
        else:
            return False