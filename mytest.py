from datetime import date
from car import Car
from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex

car1 = Glissade(date.today(), date(2021,7,18), 191000, 120000, [0.7,0.8,0.2,0.9])
print(car1.needs_service())
print(car1.tire_should_be_serviced())
