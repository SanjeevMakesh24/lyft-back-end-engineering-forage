from datetime import datetime, date

class SpindlerBattery:

    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def battery_should_be_serviced(self):
        two_years = date(self.last_service_date.year + 2, self.last_service_date.month, self.last_service_date.day)

        if self.current_date >= two_years:
            return True
        else:
            return False

    def battery_type(self):
        return "Spindler Engine"
