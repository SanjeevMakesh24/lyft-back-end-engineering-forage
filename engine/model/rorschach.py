from datetime import datetime
from engine.battery.nubbin_battery import NubbinBattery
from engine.willoughby_engine import WilloughbyEngine
from car import Car
from engine.tires.carrigan_tire import CarriganTire


class Rorschach(WilloughbyEngine, Car, NubbinBattery, CarriganTire):

    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage, tire):
        super().__init__(current_mileage, last_service_mileage)
        Car.__init__(self, current_date, last_service_date, current_mileage, last_service_mileage, tire)
        NubbinBattery.__init__(self, current_date, last_service_date)
        #New Criteria - Carrigan Tire
        CarriganTire.__init__(self, tire)

    def needs_service(self):
        if self.battery_should_be_serviced() or self.engine_should_be_serviced() or self.tire_should_be_serviced():
            return True
        else:
            return False
