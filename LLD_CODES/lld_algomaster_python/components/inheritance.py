'''

'''

class Car:
    def __init__(self):
        self.make = None
        self.model = None
    
    def start(self):
        print('engine started')
    
    def stop(self):
        print("engine stopped")

class ElectricCar(Car):
    def charge_battery(self):
        print('charge battery')

class GasCar(Car):
    def fill_gas(self):
        print('fill gas')
