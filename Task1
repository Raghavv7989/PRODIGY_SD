def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def convert_temperature(value, unit):
    unit = unit.lower()
    if unit == "c" or unit == "celsius":
        f = celsius_to_fahrenheit(value)
        k = celsius_to_kelvin(value)
        print(f"\n{value}° Celsius = {f:.2f}° Fahrenheit")
        print(f"{value}° Celsius = {k:.2f} Kelvin")
    elif unit == "f" or unit == "fahrenheit":
        c = fahrenheit_to_celsius(value)
        k = fahrenheit_to_kelvin(value)
        print(f"\n{value}° Fahrenheit = {c:.2f}° Celsius")
        print(f"{value}° Fahrenheit = {k:.2f} Kelvin")
    elif unit == "k" or unit == "kelvin":
        c = kelvin_to_celsius(value)
        f = kelvin_to_fahrenheit(value)
        print(f"\n{value} Kelvin = {c:.2f}° Celsius")
        print(f"{value} Kelvin = {f:.2f}° Fahrenheit")
    else:
        print("\nInvalid unit entered. Please enter C, F, or K.")

# Main Program
print("🌡️ Temperature Converter - PRODIGY INFOTECH TASK-01")
try:
    temp = float(input("Enter the temperature value: "))
    unit = input("Enter the unit (C, F, K): ")
    convert_temperature(temp, unit)
except ValueError:
    print("❌ Please enter a valid numeric temperature.")
