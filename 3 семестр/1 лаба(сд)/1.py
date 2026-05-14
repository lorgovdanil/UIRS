import math

x = 6.0
y = 3.0
z = 1.0
a = x**2 / (8 + x**2 / 3 + y**2 / 6)
b = x * (math.cos(x + z)**2 + 1)
print(a)
print()
print(b)
