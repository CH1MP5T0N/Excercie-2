import math
temperature = eval(input("Enter the temperature in Farenheit: "))
while not -58 <= temperature <= 41:
    print("Temperature must be between -58F and 41F")
    temperature = eval(input("Please re-enter the temperature in farenheit: "))
wind = eval(input("Enter the wind speed miles per hour: "))
while not wind >= 2:
    print("Speed must be greater than or equal to 2")
    wind = eval(input("Please re-enter the wind speed miles per hour: "))
formula = 35.74 + 0.6215 * temperature - 35.75*math.pow(wind,0.16) + 0.4275*temperature*math.pow(wind,0.16)
print(f"The wind chill index is {formula:,.3f}")