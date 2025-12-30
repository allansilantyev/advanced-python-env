import math

def rectangle_area(a, b):
    return a * b

def triangle_area(a, b):
    return 0.5 * a * b

# Ввод сторон
X = float(input("Enter side X: "))
Y = float(input("Enter side Y: "))
Z = float(input("Enter side Z: "))
T = float(input("Enter side T: "))

# Прямоугольник с прямым углом
area_rect = rectangle_area(X, Y)

# Треугольник 
area_tri = triangle_area(Z, T)

total_area = area_rect + area_tri
print(f"Area of quadrilateral = {total_area}")
