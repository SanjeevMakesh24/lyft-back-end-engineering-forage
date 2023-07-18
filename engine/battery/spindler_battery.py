from datetime import datetime, date

class SpindlerBattery:

    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def battery_should_be_serviced(self):
        #Feature Update
        #Spindler battery now requires 3 years between services instead of 2.
        three_years = date(self.last_service_date.year + 3, self.last_service_date.month, self.last_service_date.day)

        if self.current_date >= three_years:
            return True
        else:
            return False

    def battery_type(self):
        return "Spindler Engine"
