def celsius_to_farhenheit(celsius):
    farhenheit = (celsius * 9/5) + 32
    return farhenheit

celsius = int(input())
temp_farhenheit = celsius_to_farhenheit(celsius)
print(temp_farhenheit)