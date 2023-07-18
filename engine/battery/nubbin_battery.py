from datetime import datetime, date

class NubbinBattery:

    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def battery_should_be_serviced(self):
        four_years = date(self.last_service_date.year + 4, self.last_service_date.month, self.last_service_date.day)

        if self.current_date >= four_years:
            return True
        else:
            return False


    def battery_type(self):
        return "Nubbin Battery"
