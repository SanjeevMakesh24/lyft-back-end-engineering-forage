import unittest
from datetime import datetime

from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex

# **These Test Cases Do not include the new Tire Criteria, therefore they will not work**
# **However, I have done some tests in the mytest.py file, and they seem to work as intended**
class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = Calliope(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = Calliope(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = Calliope(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = Calliope(today,last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = Glissade(today,last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = Glissade(today,last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = Glissade(today,last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = Glissade(today,last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False
        current_mileage = 0
        last_service_mileage = 0

        car = Palindrome(today, last_service_date, current_mileage, last_service_mileage, warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        warning_light_is_on = False
        current_mileage = 0
        last_service_mileage = 0

        car = Palindrome(today, last_service_date, current_mileage, last_service_mileage, warning_light_is_on)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = True
        current_mileage = 0
        last_service_mileage = 0

        car = Palindrome(today, last_service_date, current_mileage, last_service_mileage, warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        current_mileage = 0
        last_service_mileage = 0

        car = Palindrome(today, last_service_date, current_mileage, last_service_mileage, warning_light_is_on)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = Rorschach(today,last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = Rorschach(today,last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = Rorschach(today,last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = Rorschach(today,last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = Thovex(today,last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = Thovex(today,last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = Thovex(today,last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = Thovex(today,last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
