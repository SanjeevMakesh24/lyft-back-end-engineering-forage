from engine.tires.tire import Tire
class OctoprimeTire(Tire):

    def tire_should_be_serviced(self):
    #Octoprime tires should be serviced only when the sum of all values in the tires wear array is greater than or equal to 3.
        if sum(self.tire_wear) >= 3:
            return True
        else:
            return False