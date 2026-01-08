'''

single under-score --> protected
double under-score --> private

'''

class Car:

    def __init__(self, brand, model):
        self._brand = brand
        self._model = model
        self._speed = 0
    
    def accelerate(self, inc):
        self._speed += inc
    
    def display(self):
        return f"{self._brand}"

car1 = Car('benz', 2010)
print(car1.display())
    
