from datetime import datetime, date
from car import Car
from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex

car1 = Thovex(date.today(), date(2018,7,18), 139000, 120000)
print(car1.needs_service())