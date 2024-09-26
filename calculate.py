import math
x = float(input("Введіть значення x:"))

y = 0.0
if x >= 5.1:
    y = math.log2(3 * x - 7) - x**(1/3) 
elif x > -0.7:
    y = math.exp(x) + 2 * x**3 - 0.7
else:
    y = (math.exp(x) + math.sin(x + math.pi / 4)) / math.exp(x)
 
print("y=", y)