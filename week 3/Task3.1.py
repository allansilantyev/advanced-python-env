import math

def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

print("Triangle 1:")
a1 = float(input("Enter leg a: "))
b1 = float(input("Enter leg b: "))

print("Triangle 2:")
a2 = float(input("Enter leg a: "))
b2 = float(input("Enter leg b: "))

c1 = hypotenuse(a1, b1)
c2 = hypotenuse(a2, b2)

print(f"Hypotenuse of triangle 1 = {c1}")
print(f"Hypotenuse of triangle 2 = {c2}")

if c1 > c2:
    print("Hypotenuse of triangle 1 is greater")
elif c1 < c2:
    print("Hypotenuse of triangle 2 is greater")
else:
    print("Both hypotenuses are equal")
