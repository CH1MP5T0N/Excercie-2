import math
mass = eval(input("Enter the mass of the cart (in kg): "))
force = eval(input("Enter the force to push the cart (in N): "))
angle = force / (mass * 9.8)
degree = math.asin(angle) * 180 / math.pi
print(f"The angle of the ramp is {round(degree,1)} degrees")