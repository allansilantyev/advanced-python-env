import math

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

# Ввод сторон и диагонали
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
d = float(input("Enter side d: "))
e = float(input("Enter diagonal e: "))

area1 = triangle_area(a, b, e)
area2 = triangle_area(c, d, e)

total_area = area1 + area2
print(f"Area of convex quadrilateral = {total_area}")
