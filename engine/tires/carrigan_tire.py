from engine.tires.tire import Tire

class CarriganTire(Tire):

    def tire_should_be_serviced(self):
        #Carrigan tires should be serviced if any of the values in the tires wear array is >= 0.9
        for wear in self.tire_wear:
            if wear >= 0.9:
                return True

        return False
