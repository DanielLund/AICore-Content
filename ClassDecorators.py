# %%
from dataclasses import dataclass

@dataclass(order=True)
class Temperature:

    __temp: float = 0.0

    def temp_to_fahrenheit(self):
        fahrenheit_temp = (self.temp * 1.8) + 32
        print(f'The fahrenheit temperature is {fahrenheit_temp}')
        return fahrenheit_temp

    @staticmethod
    def fahrenheit_to_celsius(cels):
        cels_temp = (cels - 32) / 1.8
        print(f'The temperature in celsius is {cels_temp}')
        return cels_temp

    @staticmethod
    def is_it_valid(temp):
        return -273 < temp < 3000

    @classmethod
    def from_fahrenheit(cls, temp_fahrenheit):
        return cls(Temperature.fahrenheit_to_celsius(temp_fahrenheit))
    
    @classmethod
    def standard(cls):
        return cls(0)

    @property
    def temp(self):
        return self.__temp
    
    @temp.setter
    def temp(self, value):
        print('Setting temperature')
        self.__temp = value
    
    @temp.deleter
    def temp(self):
        print('Deleting temperature')
        del self.__temp


# %%
t1 = Temperature(0)
t2 = Temperature.from_fahrenheit(32)

print(t1.temp)
print(t2.temp)

# %%
