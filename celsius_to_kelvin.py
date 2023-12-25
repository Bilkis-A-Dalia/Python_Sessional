def celsius_to_kelvin(celsius):
    kelvin = ((celsius * 9/5) + 32) + 273.15
    return kelvin

celsius = int(input())
temp_kelvin = celsius_to_kelvin(celsius)
print(temp_kelvin)