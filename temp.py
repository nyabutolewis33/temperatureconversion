import datetime

class Temperature:
    def convertFarenheit(self, celsius):
        farenheit = (celsius * 9/5) + 32
        return farenheit

    def convertCelsius(self, farenheit):
        celsius = (farenheit - 32) * 5/9
        return celsius
temperature = Temperature()

print(temperature.convertFarenheit(75))   
print(temperature.convertCelsius(97))     