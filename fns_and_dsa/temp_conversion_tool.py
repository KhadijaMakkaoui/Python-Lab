FAHRENHEIT_TO_CELSIUS_FACTOR=5/9
CELSIUS_TO_FAHRENHEIT_FACTOR=9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit-32)*FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return 32+CELSIUS_TO_FAHRENHEIT_FACTOR*celsius


temperature=float(input("Enter the temperature to convert: "))
type=input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
if type=="F":
    input(str(temperature)+"°F is "+str(convert_to_celsius(temperature))+"°C")
else:
    input(str(temperature)+"°C is "+str(convert_to_fahrenheit(temperature))+"°F")

